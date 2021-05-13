from collections import deque
import sys
input = sys.stdin.readline
##### 高速化テスト #####

mod = 10**9 + 7
INF = 10**6
N, K = map(int, input().split())
edges = [[] * N for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    edges[a].append(b)
    edges[b].append(a)
dq = deque([0])
color = [INF] * N
color[0] = K
ans = K
while dq:
    p = dq.popleft()
    cnt = 0
    for c in edges[p]:
        if color[c] == INF:
            if p == 0:
                color[c] = (K - 1 - cnt) % mod
            else:
                color[c] = (K - 2 - cnt) % mod
            ans = (ans * color[c]) % mod
            cnt += 1
            dq.append(c)
print(ans)

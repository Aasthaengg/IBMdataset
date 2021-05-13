from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9 + 7
N, K = map(int, input().split())

edges = [[] * N for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

# 0をrootとする
dq = deque([0])

visited = [False] * N
visited[0] = True

# color[i] = i番目の頂点を塗ることが可能な色の数
# 全て更新するので初期値は任意
color = [0] * N
color[0] = K

"""
root = 0 から末端に向かって調べる

子1, 子2, 子3, ...と複数の「未着色」の子がある場合、塗ることが出来る色の数は
K-1, K-2, K-3,... (p==0 の場合)
K-2, K-3, K-4,... (p!=0 の場合)　のようになる

子が十分多い場合、どこかで「0」になるので、ans = 0　となる
故に、色の数が負になっても答えには影響しない
"""

while dq:
    # 親となる頂点
    p = dq.popleft()
    # 親をpとした時の、「未着色」な子の数
    cnt = 0
    for c in edges[p]:
        if not visited[c]:
            if p == 0:
                color[c] = (K - 1 - cnt) % mod
            else:
                color[c] = (K - 2 - cnt) % mod
            cnt += 1
            visited[c] = True
            dq.append(c)

ans = 1
for i in range(N):
    ans = (ans * color[i]) % mod

print(ans)

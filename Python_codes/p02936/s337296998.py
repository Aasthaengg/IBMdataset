from collections import deque

N, Q = list(map(int,input().split()))
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
p = [0 for _ in range(N)]
for i in range(Q):
    in1, in2 = list(map(int,input().split()))
    p[in1 - 1] += in2

ans = [0 for _ in range(N)]
ans[0] = p[0]

def bfs(s):
    q = deque([s])
    seen = [False] * N
    
    while(q):
        node = q.popleft()
        seen[node] = True
        for nx in G[node]:
            if seen[nx] == False:
                q.append(nx)
                ans[nx] += (p[nx] + ans[node])

bfs(0)
print(*ans)
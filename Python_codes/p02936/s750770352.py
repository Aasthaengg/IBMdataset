import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)
point = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    point[p-1] += x
q = deque([[0, -1, point[0]]])
done = [-1]*N
while q:
    cur, fr, p = q.popleft()
    done[cur] = p
    for nex in G[cur]:
        if nex == fr: continue
        q.append([nex, cur, p+point[nex]])
ans = []
for i in range(N):
    ans.append(done[i])
print(*ans)

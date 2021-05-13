from collections import deque
import sys
sys.setrecursionlimit(1000000000)
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
que = deque([0])
parent = [-1]*N
parent[0] = 0
while que:
    cur = que.pop()
    for nxt in edges[cur]:
        if parent[nxt] < 0:
            parent[nxt] = cur
            que.append(nxt)
cur = N-1
route = [N-1]
while cur:
    cur = parent[cur]
    route.append(cur)
i = len(route)//2
a, b = route[i-1:i+1]
edges[a].remove(b)
edges[b].remove(a)
que = deque([0])
flag = [True]*N
score = 0
flag[0] = False
while que:
    v0 = que.pop()
    score+=1
    for v in edges[v0]:
        if flag[v]:
            que.append(v)
            flag[v] = False
if score>N//2:
    print('Fennec')
else:
    print('Snuke')
N, M, P = map(int, input().split())
Edges = []
pos = [[] for _ in range(N)]
neg = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    Edges.append((a-1, b-1, P-c))
    pos[a-1].append(b-1)
    neg[b-1].append(a-1)

from collections import deque

def dfs(s, lis):
    checked = [0]*N
    stack = deque([(s, 0)])
    while stack:
        v, c = stack.pop()
        if checked[v]!=0:
            continue
        checked[v] = 1
        for i in lis[v]:
            if checked[i]==0:
                stack.append((i, c+1))
    return checked

posc = dfs(0, pos)
negc = dfs(N-1, neg)
used = [0]*N
for i, (p, n) in enumerate(zip(posc, negc)):
    if p and n:
        used[i] = 1

def BellmanFord(s):
    inf = 10**18
    dist=[inf for i in range(N)]
    dist[s]=0
    for i in range(N):
        for edge in Edges:
            if used[edge[0]]==0 or used[edge[1]]==0:
                continue
            if edge[0] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                if i>=N-1:
                    return []
    return dist

d = BellmanFord(0)
if len(d)==0:
    print(-1)
else:
    print(max(0, -d[-1]))
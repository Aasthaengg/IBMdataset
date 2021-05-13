import collections
from collections import deque

def Dfs(now):
    flag = True
    d = deque()
    d.append(now)
    visited[now]=0
    while len(d):
        now = d.pop()
        for i,j in vec[now]:
            if visited[i]==INF:
                d.append(i)
                visited[i]=visited[now]+j
            else:
                if visited[i]==visited[now]+j:
                    continue
                else:
                    flag=False
                    break
    return flag


n,m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
vec= [[] for i in range(n)]

for i in range(m):
    vec[a[i][0]-1].append((a[i][1]-1,a[i][2]))
    vec[a[i][1]-1].append((a[i][0]-1,-a[i][2]))

INF=float('inf')
visited=[INF]*n

for i in range(n):
    if visited[i]==INF:
        if not Dfs(i):
            print('No')
            exit()
print('Yes')
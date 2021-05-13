import collections
from collections import deque
import sys
input = sys.stdin.readline
 
def bfs(s):
    d = deque()
    d.append(s)
    dis[s]=0
    flag=True
    while len(d):
        x = d.popleft()
        for i,j in vec[x]:
            if dis[i] == INF:
                dis[i]=dis[x]+j
                d.append(i)
 
            else:
                if dis[i]==dis[x]+j:
                    continue
                else:
                    print('No')
                    exit()
    return flag
 
 
n,m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
vec= [[] for i in range(n)]
 
for i in range(m):
    vec[a[i][0]-1].append((a[i][1]-1,a[i][2]))
    vec[a[i][1]-1].append((a[i][0]-1,-a[i][2]))
 
INF=float('inf')
dis=[INF]*n
 
for i in range(n):
    if dis[i]==INF:
        bfs(i)
print('Yes')
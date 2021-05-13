import collections
from collections import deque
def tree(s,m):
    INF=-10**9
    visited = [INF for i in range(n)]

    def bfs():
        d = deque()
        d.append(s)
        ans=m
        mod=10**9+7
        count=0
        visited[s]=0
        while len(d):
            v = m
            x = d.popleft()
            if count<2:
                count+=1
            v-=count
            for i in range(len(b[x])):
                y=b[x][i]
                if visited[y] == INF:
                    visited[y]=0
                    d.append(y)
                    ans*=v
                    ans%=mod
                    v-=1
        return ans
    return bfs()



n,m= map(int, input().split())
a = [list(map(int, input().split())) for i in range(n-1)]
b = [[] for i in range(n)]

for i in range(n-1):
    b[a[i][0]-1].append(a[i][1]-1)
    b[a[i][1]-1].append(a[i][0]-1)

c=tree(0,m)
print(c)
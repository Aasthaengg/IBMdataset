n,m= map(int, input().split())
a= [list(map(int, input().split())) for i in range(m)]
s,t= map(int, input().split())

b= [[] for i in range(3*n)]
# 3で割り切れる数がもとの点
for i in range(m):
    b[3*(a[i][0]-1)].append(3*(a[i][1]-1)+1)
    b[3*(a[i][0]-1)+1].append(3*(a[i][1]-1)+2)
    b[3*(a[i][0]-1)+2].append(3*(a[i][1]-1))

import collections
from collections import deque
def tree(s,g):

    INF=-10**9
    dis = [INF for i in range(3*n)]
    dis[s]=0
    def bfs():
        d = deque()
        d.append(s)

        while len(d):
            x = d.popleft()

            for i in range(len(b[x])):
                y=b[x][i]
                if dis[y] == INF:
                    d.append(y)
                    dis[y]=dis[x]+1


        return dis[g]
    return bfs()

ans=tree(3*(s-1),3*(t-1))
if ans==-10**9:
    print(-1)
else:
    print(ans//3)
import sys
input = sys.stdin.readline

n,u,v= map(int, input().split())
a= [list(map(int, input().split())) for i in range(n-1)]
b = [[] for i in range(n)]

for x,y in a:
    b[x-1].append(y-1)
    b[y-1].append(x-1)

import collections
from collections import deque
def tree(s):

    INF=-10**9
    dis = [INF for i in range(n)]
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


        return dis
    return bfs()

# q1:高橋くんからの最短距離、q2:青木君からの最短距離
q1=tree(u-1)
q2=tree(v-1)
ans=0

for i in range(n):
    if q2[i]>q1[i]:
        ans=max(q2[i],ans)
print(ans-1)

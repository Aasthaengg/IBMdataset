import sys
input = sys.stdin.readline

n=int(input())
a= [list(map(int, input().split())) for i in range(n-1)]
b = [[] for i in range(n)]

for x,y in a:
    b[x-1].append(y-1)
    b[y-1].append(x-1)

# グラフでのbfs
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

fennec=tree(0)
snuke=tree(n-1)

# ans1:fennecの取り分
# ans2:sunukeの取り分
ans1=0
ans2=0
for i in range(n):
    if fennec[i]<=snuke[i]:
        ans1+=1
    else:
        ans2+=1

if ans1>ans2:
    print('Fennec')
else:
    print('Snuke')
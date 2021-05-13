import sys
import collections
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10000000)

n = int(input())
g = [[]for i in range(n)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    u-=1
    v-=1
    g[u].append([v,w])
    g[v].append([u,w])
lis = [-1 for i in range(n)]
def dfs(i,j,color):
    for nec,leng in g[i]:
        if nec==j:continue
        if leng%2==0:
            lis[nec] = color
            dfs(nec,i,color)
        else:
            lis[nec] = 1-color
            dfs(nec,i,1-color)
lis[0]=0
dfs(0,-1,0)

for i in range(n):
    print(lis[i])

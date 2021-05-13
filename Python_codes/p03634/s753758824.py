import sys
sys.setrecursionlimit(10**9)
n=int(input())
l=[[] for i in range(n)]
C=[0]*n
for i in range(n-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    l[a].append([b,c])
    l[b].append([a,c])
def dfs(now,par,cost):
    C[now]=cost
    L=l[now]
    for i in range(len(L)):
        if L[i][0]==par:
            continue
        dfs(L[i][0],now,cost+L[i][1])
Q,K=map(int,input().split())
K-=1
dfs(K,K,0)
for i in range(Q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    print(C[x]+C[y])
import sys
sys.setrecursionlimit(1000000000)
INF=10**9
n,a,b,c=map(int,input().split())
l=[int(input()) for i in range(n)]
def dfs(i,x,y,z):
    if i==n:
        if min(x,y,z)>0:
            return abs(x-a)+abs(y-b)+abs(z-c)-30
        else:
            return INF
    ans=dfs(i+1,x,y,z)
    ant=dfs(i+1,x+l[i],y,z)+10
    anu=dfs(i+1,x,y+l[i],z)+10
    anv=dfs(i+1,x,y,z+l[i])+10
    return min(ans,ant,anu,anv)
print(dfs(0,0,0,0))
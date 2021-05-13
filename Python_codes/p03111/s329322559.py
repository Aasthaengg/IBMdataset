from sys import stdin
#入力
readline=stdin.readline
inf=10**9
n,a,b,c=map(int,readline().split())
l=[int(readline()) for _ in range(n)]

def dfs(now,x,y,z):
    if now==n:
        return abs(a-x)+abs(b-y)+abs(c-z)-30 if min(x,y,z)>0 else inf
    else:
        res1=dfs(now+1,x,y,z)
        res2=dfs(now+1,x+l[now],y,z)+10
        res3=dfs(now+1,x,y+l[now],z)+10
        res4=dfs(now+1,x,y,z+l[now])+10
        return min(res1,res2,res3,res4)

print(dfs(0,0,0,0))
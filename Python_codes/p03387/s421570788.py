import sys
sys.setrecursionlimit(1000000)

a,b,c=map(int,input().split())
ans=0
def dfs(x,y,z):
    global ans
    if x==y==z:
        print(ans)
    elif x==y and x<z:
        ans+=1
        dfs(x+1,y+1,z)
    elif y==z and y<x:
        ans+=1
        dfs(x,y+1,z+1)
    elif x==z and x<y:
        ans+=1
        dfs(x+1,y,z+1)
    elif x<y<=z or x<z<=y:
        ans+=1
        dfs(x+2,y,z)
    elif y<x<=z or y<z<=x:
        ans+=1
        dfs(x,y+2,z)
    elif z<x<=y or z<y<=x:
        ans+=1
        dfs(x,y,z+2)
dfs(a,b,c)
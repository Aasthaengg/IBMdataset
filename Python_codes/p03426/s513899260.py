import sys
sys.setrecursionlimit(10**7)
h,w,d=map(int,input().split())
pos=[0]*(h*w+1)
for i in range(h):
    a=list(map(int,input().split()))
    for j in range(w):
        pos[a[j]]=(i,j)
ans=[0]*(h*w+1)
visited=[True]*(h*w+1)
def dfs(s,nxt):
    if nxt>h*w:
        return 
    visited[s]=False
    dfs(nxt,nxt+d)
    x,y=pos[s]
    nx,ny=pos[nxt]
    ans[s]+=ans[nxt]+abs(nx-x)+abs(ny-y)
for i in range(1,h*w+1):
    if visited[i]:
        dfs(i,i+d)
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(ans[l]-ans[r])
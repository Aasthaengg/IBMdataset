def dfs(n):
    ans=0
    nn=n*2
    if nn<=y:
        ans+=1
        ans+=dfs(nn)
    return ans
x,y=map(int,input().split())
print(dfs(x)+1)
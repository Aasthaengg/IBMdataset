n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
def dfs(cur,x,y,z):
    if cur == n:
        return abs(a-x) + abs(b-y) + abs(c-z)-30 if min(x,y,z) > 0 else 10**9
    ret1 = dfs(cur+1,x,y,z)
    ret2 = dfs(cur+1,x+l[cur],y,z) + 10
    ret3 = dfs(cur+1,x,y+l[cur],z) + 10
    ret4 = dfs(cur+1,x,y,z+l[cur]) + 10
    return min(ret1,ret2,ret3,ret4)
print(dfs(0,0,0,0))
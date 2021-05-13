def dfs(cnt,a,b,c):
    if cnt == N:
        _sum = abs(A-a) + abs(B-b) + abs(C-c) - 30
        return _sum if min(a,b,c) > 0 else 10**9
    ret0 = dfs(cnt+1, a, b, c)
    ret1 = dfs(cnt+1, a+l[cnt] , b, c) + 10
    ret2 = dfs(cnt+1, a, b+l[cnt], c) + 10
    ret3 = dfs(cnt+1, a, b, c+l[cnt]) + 10
    return min(ret0,ret1,ret2,ret3) 
    
N,A,B,C,*l = map(int,open(0).read().split())
print(dfs(0,0,0,0))
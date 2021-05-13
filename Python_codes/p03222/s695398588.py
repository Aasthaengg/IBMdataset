H,W,K=map(int,input().split())
mod=10**9+7
fib=[1,1,2,3,5,8,13,21]

from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(cur,now):
    if cur==H:
        if now==K:
            return 1
        else:
            return 0
    elif now==1:
        if W==1:
            return dfs(cur+1,1)%mod
        else:
            return (fib[W-1]*dfs(cur+1,1)+fib[W-2]*dfs(cur+1,2))%mod
    elif now==W:
        return (fib[W-2]*dfs(cur+1,W-1)+fib[W-1]*dfs(cur+1,W))%mod
    else:
        return (fib[W-now]*fib[now-2]*dfs(cur+1,now-1)+fib[W-now]*fib[now-1]*dfs(cur+1,now)+fib[W-now-1]*fib[now-1]*dfs(cur+1,now+1))%mod
    
print(dfs(0,1))
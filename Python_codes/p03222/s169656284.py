H,W,K=map(int,input().split())
mod=10**9+7
fib=[1,1,2,3,5,8,13,21]
memo=[[None]*W for _ in range(H+1)]
def dfs(cur,now):
    if cur==H:
        if now==K:
            return 1
        else:
            return 0
    elif now==1:
        if W==1:
            if memo[cur+1][0]==None:
                memo[cur+1][0]=dfs(cur+1,1)%mod
            return memo[cur+1][0]
        else:
            if memo[cur+1][0]==None:
                memo[cur+1][0]=dfs(cur+1,1)%mod
            if memo[cur+1][1]==None:
                memo[cur+1][1]=dfs(cur+1,2)%mod
            return (fib[W-1]*memo[cur+1][0]+fib[W-2]*memo[cur+1][1])%mod
    elif now==W:
        if memo[cur+1][W-2]==None:
            memo[cur+1][W-2]=dfs(cur+1,W-1)%mod
        if memo[cur+1][W-1]==None:
            memo[cur+1][W-1]=dfs(cur+1,W)%mod            
        return (fib[W-2]*memo[cur+1][W-2]+fib[W-1]*memo[cur+1][W-1])%mod
    else:
        if memo[cur+1][now-2]==None:
            memo[cur+1][now-2]=dfs(cur+1,now-1)%mod
        if memo[cur+1][now-1]==None:
            memo[cur+1][now-1]=dfs(cur+1,now)%mod     
        if memo[cur+1][now]==None:
            memo[cur+1][now]=dfs(cur+1,now+1)%mod  
        return (fib[W-now]*fib[now-2]*memo[cur+1][now-2]+fib[W-now]*fib[now-1]*memo[cur+1][now-1]+fib[W-now-1]*fib[now-1]*memo[cur+1][now])%mod
    
print(dfs(0,1))
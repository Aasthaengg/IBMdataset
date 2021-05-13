import sys
sys.setrecursionlimit(10**8)
n,k = map(int,input().split())
ki = [[]for _ in range(n)]
mod = 10**9+7
fact = [1]*(max(n,k)+1)
for i in range(1,max(n,k)+1):
    fact[i] = (fact[i-1]*i)%mod
invfact = [1]*(max(n,k)+1)
invfact[-1] = pow(fact[-1],mod-2,mod)
for i in range(max(n,k)-1,0,-1):
    invfact[i] = (invfact[i+1]*(i+1))%mod

def P(a,b,mod):
    return (fact[a]*invfact[a-b])%mod
    
for i  in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)

    

def dfs(now,last = -1):
    res = 1
    
    if last != -1:
        if len(ki[now]) == 1:return 1
        res = P(k-2,len(ki[now])-1,mod)
        if k-1 < len(ki[now]):res = 0
    for next in ki[now]:
        if next == last:continue
        res *= dfs(next,now)
    return res
ans = dfs(0,-1)

ans *= P(k,len(ki[0])+1,mod)
ans %= mod
if(len(ki[0])+1>k):ans = 0
print(ans)
            

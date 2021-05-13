import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,k=map(int,input().split())
l=[[] for _ in range(n)]
ans=k
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    l[a].append(b)
    l[b].append(a)

mod=10**9+7
fact=[1]
fact_inv=[1]
for i in range(10**5+1):#<< Nの最大値
    new_fact=fact[-1]*(i+1)%mod
    fact.append(new_fact)
    fact_inv.append(pow(new_fact,mod-2,mod))

def mod_p(n,k,mod):
    if n-k<0:
        print(0)
        exit()
    return fact[n]*fact_inv[n-k]%mod

def dfs(v,p):
    ans2=1
    for a in l[v]:
        if a==p:
            continue
        ans2*=dfs(a,v)
        ans2%=mod
    return mod_p(k-2,len(l[v])-1,mod)*ans2%mod

ans*=mod_p(k-1,len(l[0]),mod)

for a in l[0]:
    ans*=dfs(a,0)

print(ans%mod)

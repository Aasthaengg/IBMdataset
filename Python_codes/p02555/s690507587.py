s=int(input())
mod=10**9+7
p=[1]
for i in range(1,2001):
    a=p[-1]*i
    a%=mod
    p.append(a)
ans=0
for i in range(1,s//3+1):
    k=s-i*3
    n=k+i-1
    ans+=p[n]*pow(p[i-1],mod-2,mod)*pow(p[k],mod-2,mod)
    ans%=mod
print(ans)
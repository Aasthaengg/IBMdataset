def combinations(n,k,mod):
    x,y = 1,1
    for i in range(k):
        x = (x*(n-i))%mod
        y = (y*(i+1))%mod
    return (x*pow(y,mod-2,mod))%mod
    

mod = 10**9+7
n,k = map(int,input().split())

def cmap(n,k):
    x = [1]
    y = [1]
    c = [1]
    for i in range(k+1):
        x.append((x[i]*(n-i))%mod)
        y.append((y[i]*(i+1))%mod)
        c.append((x[i+1]*pow(y[i+1],mod-2,mod))%mod)
    return c
    
#print(cmap(n,n))
nc=cmap(n,n-1)
n1c=cmap(n-1,n-2)

ans = 0
for i in range(min(n-1,k)+1):
    ans = (ans+(nc[i]*n1c[i]))%mod

print(ans)
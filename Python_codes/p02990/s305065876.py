n,k = map(int,input().split()) # k>p の時 最大値p+1
p = n-k
mod = 10**9 + 7
def kai(n):
    p = 1
    for i in range(1,n+1):
        p = p*i % mod
    return p
def com(n,k):
    s = 0
    if n < k :
        return 0
    else:
        s = kai(n)*(pow(kai(k),mod-2,mod))*(pow(kai(n-k),mod-2,mod))
        return s%mod
for i in range(1,k+1):
    print(com(p+1,i)*com(k-1,i-1)%mod)
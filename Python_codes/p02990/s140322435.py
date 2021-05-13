mod = 10**9 + 7
def comb(N,x):
    numerator = 1
    for i in range(N-x+1,N+1):
        numerator = numerator * i % mod
    denominator = 1
    for j in range(1,x+1):
        denominator = denominator * j % mod
    d = pow(denominator,mod-2,mod)
    return numerator * d % mod

n,k = map(int,input().split())

for i in range(1,k+1):
    print(comb(n-k+1,i)*comb(k-1,i-1)%mod)
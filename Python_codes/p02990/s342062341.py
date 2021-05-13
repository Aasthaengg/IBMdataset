n,k=map(int,input().split())

mod=10**9+7
for i in range(1,k+1):
    numerator=(n-k+1)%mod
    denominator=i
    for j in range(1,i):
        numerator=(((numerator*(j+n-k+1-i))%mod)*(j+k-i))%mod
        denominator=(denominator*j*j)%mod
    print((numerator*(pow(denominator,mod-2,mod)))%mod)
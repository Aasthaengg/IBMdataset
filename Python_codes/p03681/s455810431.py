from math import factorial

N,M=map(int,input().split())
if abs(N-M)>1:
    print(0)
else:
    if N==M:
        mod=10**9+7
        n=factorial(N)%mod
        m=factorial(M)%mod
        print(n*m*2%mod)
    else:
        mod=10**9+7
        n=factorial(N)%mod
        m=factorial(M)%mod
        print(n*m%mod)
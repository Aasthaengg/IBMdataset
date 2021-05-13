def f(L):
    X=0
    for k in L:
        X+=2**(k-1)
    return X

N,M=map(int,input().split())
H=2**N
inf=float("inf")

DP=[inf for _ in range(H)]
DP[0]=0

for _ in range(M):
    A,B=map(int,input().split())
    C=f(list(map(int,input().split())))

    for k in range(H):
        DP[k|C]=min(DP[k|C],DP[k]+A)

if DP[-1]==inf:
    print(-1)
else:
    print(DP[-1])
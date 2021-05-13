from math import gcd

N,K=map(int,input().split())
A=list(map(int,input().split()))

ans=["POSSIBLE","IMPOSSIBLE"]

if max(A)<K:
    print(ans[1])
else:
    g=A[-1]
    for i in range(N-1):
        g=gcd(g,A[i])
    if K%g==0:
        print(ans[0])
    else:
        print(ans[1])
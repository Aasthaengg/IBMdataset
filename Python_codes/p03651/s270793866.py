from math import gcd
N,K=map(int,input().split())
A=list(map(int,input().split()))
g=A[0]
if max(A)<K:
    print('IMPOSSIBLE')
    exit()
for i in range(1,N):
    g=gcd(g,A[i])

for i in range(N):
    if (A[i]-K)%g==0:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
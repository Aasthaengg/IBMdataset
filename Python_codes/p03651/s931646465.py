from math import gcd

N,K=map(int,input().split())
A=list(map(int,input().split()))

G=A[0]
for a in A:
    G=gcd(G,a)

F=False
for a in A:
    if a>=K and (K-a)%G==0:
        F=True

if F:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
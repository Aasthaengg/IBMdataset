from math import gcd
N=int(input())
A=list(map(int,input().split()))

G=A[0]
for b in A:
    G=gcd(G,b)
print(G)
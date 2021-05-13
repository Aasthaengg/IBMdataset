from fractions import gcd
N,K=map(int, input().split())
A=list(map(int, input().split()))
if K in A:
    print("POSSIBLE")
    exit()
if K>max(A):
    print("IMPOSSIBLE")
    exit()

for i in range(N-1):
    if i==0:
        G=gcd(A[0],A[1])
    else:
        G=gcd(G, A[i+1])
#print(G)
if K%G==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

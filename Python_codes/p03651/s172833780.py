import fractions
N,K=map(int,input().split())
A=list(map(int,input().split()))
gc=A[0]
for i in range(1,N):
    gc=fractions.gcd(gc,A[i])
#print(gc)
A.sort()
if (K<=A[N-1])and(((A[N-1]-K)%gc)==0)and((K%gc)==0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
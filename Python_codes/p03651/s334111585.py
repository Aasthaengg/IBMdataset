import fractions

n,k=map(int,input().split())
A=list(map(int,input().split()))

M=A[0]
g=A[0]
for i in range(n-1):
    M=max(M,A[i+1])
    g=fractions.gcd(g,A[i+1])

if k<=M:
    if g==1:
        print("POSSIBLE")
    elif k%g==0:
            print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
else:
    print("IMPOSSIBLE")
def gcd(a,b):
    if b>a:
        a,b = b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,K = map(int,input().split())
A = list(map(int,input().split()))

mm = A[0]

for i in range(1,N):
    mm = gcd(mm,A[i])

for i in range(N):
    if A[i]-K>=0 and (A[i]-K)%mm==0:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")




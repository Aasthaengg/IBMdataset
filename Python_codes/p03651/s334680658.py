import fractions
n,k=map(int,input().split())
a=list(map(int,input().split()))
if max(a)<k:
    print("IMPOSSIBLE")
    exit()
t=a[0]
if n!=1:
    for i in range(1,n):
        t=fractions.gcd(t,a[i])

if k%t==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


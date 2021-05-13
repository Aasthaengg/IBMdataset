import fractions
N,K=map(int,input().split())
a=list(map(int,input().split()))
bef=a[0]
gcd=a[0]
max_=a[0]
for i in range(1,N):
    if max_<a[i]:
        max_=a[i]
    gcd=fractions.gcd(gcd,a[i])
if max_<K:
    print("IMPOSSIBLE")
else:
    if K%gcd==0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
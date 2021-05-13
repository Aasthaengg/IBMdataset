import fractions
n,*a=map(int,open(0).read().split())
e=fractions.gcd(a[0],a[1])
for i in range(1,n):
    e=fractions.gcd(e,a[i])

print(e)
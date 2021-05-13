import fractions
a,b=map(int,input().split())
g=fractions.gcd(a, b)
l=int(a*b/g)
print(l)
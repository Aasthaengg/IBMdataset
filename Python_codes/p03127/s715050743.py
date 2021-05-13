import fractions
n=int(input())
n=list(map(int,input().split()))
p=n[0]
for x in n:
    p=fractions.gcd(p,x)
print(p)
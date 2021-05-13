import fractions
a,b = map(int,input().split())
if (a < b):
    if b % a == 0:
        print(b)
    else:
        print(b * (a // fractions.gcd(a, b)))
else:
    if a % b == 0:
        print(a)
    else:
        print(a * (b // fractions.gcd(a, b)))

import fractions

a,b = list(map(int, input().split()))

print(int(a * b / fractions.gcd(a,b)))
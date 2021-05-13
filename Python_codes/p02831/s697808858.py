import fractions

a , b = (int(x) for x in input().split())

result = fractions.gcd(a, b)

print((a * b) // result)
import fractions

A, B = map(int, input().split())
gcd_ = fractions.gcd(A, B)
res = (A * B) / gcd_
print(int(res))
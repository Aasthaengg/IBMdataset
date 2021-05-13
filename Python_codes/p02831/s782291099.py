import fractions

A, B = map(int, input().split())
lcm = A * B // fractions.gcd(A, B)
print(lcm)

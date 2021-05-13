import fractions

n = int(input())
lcm = 1

for i in range(n):
    t = int(input())
    lcm = lcm*t//fractions.gcd(lcm, t)

print(lcm)
import fractions
def lcm(a):
    LCM = a[0]
    for i in range(1, n):
        LCM = LCM * a[i] // fractions.gcd(LCM, a[i])
    return LCM

n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

print(lcm(t))
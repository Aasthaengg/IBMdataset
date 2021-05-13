import fractions
def lcm(a):
    LCM = a[0]
    for i in range(1, n):
        LCM = LCM * a[i] // fractions.gcd(LCM, a[i])
    return LCM

n = int(input())
a = list(map(int, input().split()))

m = lcm(a) - 1
ans = 0

for i in range(n):
    ans += m%a[i]

print(ans)
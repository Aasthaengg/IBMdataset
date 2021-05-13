import fractions
mod = 10 ** 9 + 7

def lcm(a,b):
    return (a * b) // fractions.gcd(a, b)

n = input()
a = list(map(int, input().split()))

LCM = 1
for i in a:
    LCM = lcm(LCM,i)

ans = 0
for i in a:
    ans += LCM // i
print(ans % mod)


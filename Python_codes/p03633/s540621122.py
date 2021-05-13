from fractions import gcd
n = int(input())
t = list(int(input()) for _ in range(n))


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1
for i in t:
    ans = lcm(ans, i)

print(ans)
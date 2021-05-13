n = int(input())
t = [int(input()) for _ in range(n)]


def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b


def lcm(a, b):
    return (a * b) // gcd(a, b)


ans = t[0]
for i in range(1, n):
    ans = lcm(ans, t[i])
print(ans)
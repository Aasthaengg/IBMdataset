def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ans = a[0]
for x in range(1, n):
    ans = lcm(ans, a[x])

print(ans)

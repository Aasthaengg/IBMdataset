n, m = map(int, input().split())
s = input()
t = input()

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x // gcd(x, y) * y

g = gcd(n, m)
bl = True
for k in range(g):
    i, j = k * n // g, k * m // g
    if s[i] != t[j]: # s[i] != s[j] にしてた...
        bl = False

print(lcm(n, m)) if bl else print('-1')
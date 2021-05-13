import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n, m = map(int, input().split())
s = input()
t = input()
d = dict()
f = True

g = lcm(n, m)
nn = g // n
mm = g // m

for i in range(n):
    d[1 + nn * i] = s[i]

for i in range(m):
    if 1+mm*i in d:
        if d[1+mm * i] != t[i]:
            f = False
if f:
    print(g)
else:
    print(-1)
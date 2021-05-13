def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


n, k = map(int, input().split(), )
a = [ int(x) for x in input().split() ]

g = 0
for aa in a:
    g = gcd(g, aa)

print("POSSIBLE" if k <= max(a) and k%g == 0 else "IMPOSSIBLE")

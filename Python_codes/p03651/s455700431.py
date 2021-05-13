def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a


n, k = map(int, input().split())
a = list(map(int, input().split()))

m = max(a)

g = a[0]

for i in range(n):
    g = gcd(g, a[i])

if k > m:
    print("IMPOSSIBLE")
elif k % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

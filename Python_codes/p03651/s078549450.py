from fractions import gcd

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
if max(a) < k:
    print("IMPOSSIBLE")
    exit()
x = a[0]
for i in range(1,n):
    x = gcd(x, a[i])

print("IMPOSSIBLE" if k % x else "POSSIBLE")

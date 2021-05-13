from math import gcd
n, k = map(int, input().split())
a = list(map(int, input().split()))
if max(a) < k:
    print("IMPOSSIBLE")
    exit()
if k in a:
    print("POSSIBLE")
    exit()
a_gcd = a[0]
for i in range(1, n):
    a_gcd = gcd(a_gcd, a[i])

if k % a_gcd == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

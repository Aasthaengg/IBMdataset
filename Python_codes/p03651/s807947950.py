from math import gcd
n, k = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort(); b = a[0]
for i in range(1, len(a)): b = gcd(b, a[i])
if len(a) == 1:
    print("POSSIBLE") if k == a[0] else print("IMPOSSIBLE")
else:
    print("POSSIBLE") if k <= a[-1] and k%b == 0 else print("IMPOSSIBLE")
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))
if k > max(a):
    print("IMPOSSIBLE")
else:
    gcd = 0
    for i in range(n):
        gcd = math.gcd(gcd, a[i])
    if k % gcd == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
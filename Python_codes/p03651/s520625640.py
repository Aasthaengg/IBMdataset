import functools
import fractions

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = max(a)

if k > m:
    print("IMPOSSIBLE")
else:
    gcd = functools.reduce(fractions.gcd, a)
    if k % gcd == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

import math
import functools
n, k = map(int, input().split())
a = list(map(int, input().split()))
a_max = max(a)
G = functools.reduce(math.gcd, a)
ok = True
if k > a_max:
    ok = False
else:
    if k%G == 0:
        pass
    else:
        ok = False

if ok:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

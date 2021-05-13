from functools import reduce
from fractions import gcd

POSSIBLE = "POSSIBLE"
IMPOSSIBLE = "IMPOSSIBLE"
n, k = map(int, input().split())
a = list(map(int, input().split()))

# max(a) < k → だめ
# N == 1 ぴったじゃなきゃだめ
# N > 1
## 互いに素な数が含まれている → ○
## 含まれてないが、kがその倍数 → ○
if max(a) < k:
    print(IMPOSSIBLE)
    exit()
if n == 1:
    if k == a[0]:
        print(POSSIBLE)
    else:
        print(IMPOSSIBLE)
else:
    g = reduce(lambda a, b: gcd(a, b), a)
    if g == 1:
        print(POSSIBLE)
    else:
        if k % g == 0:
            print(POSSIBLE)
        else:
            print(IMPOSSIBLE)


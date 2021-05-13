n = int(input())
a = list(map(int, input().split()))

from collections import Counter

c = Counter(a)

if c[0] > 0:
    if len(c) == 1:
        bl = True
    else:
        if len(c) > 2:
            bl = False
        else:
            bl = (n == 3 * c[0])
else:
    se = set(c.keys())
    if len(se) != 3:
        bl = False
    else:
        bl = True
        xor = 0
        for key in se:
            xor ^= key
            if c[key] * 3 != n:
                bl = False
        if xor != 0:
            bl = False

print('Yes') if bl else print('No')
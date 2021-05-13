import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

import numpy as np
a = np.array(ri_())
ans = 0
while True:
    if np.any(a % 2 == 1):
        break
    if a[0] == a[1] and a[1] == a[2]:
        ans = -1
        break
    a = (sum(a) - a) // 2
    ans += 1
print(ans)
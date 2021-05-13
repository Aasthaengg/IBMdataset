import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(input())
P = inpl()
mn = 1001001001
ans = 0
for i in P:
    mn = min(mn, i)
    if i == mn:
        ans += 1
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

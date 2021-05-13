import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, K = inpl()
H = inpl()
H.sort()
H.reverse()
for i in range(K):
    if len(H) == i:
        break
    H[i] = 0
print(sum(H))

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

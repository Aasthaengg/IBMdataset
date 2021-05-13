import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, M, K = inpl()
A = inpl()
B = inpl()
ib = M
a = 0
b = sum(B)
ans = 0
for i in range(N+1):
    if i != 0:
        a += A[i-1]
    if a > K:
        break
    while a+b > K:
        if ib > 0:
            ib -= 1
            b -= B[ib]
        else:
            break
    ans = max(ans, i+ib)
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

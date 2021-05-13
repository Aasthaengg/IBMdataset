import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

A, B, K = map(int, input().split())
ans = []
for i in range(1, min(A, B)+1):
	if A%i == 0 and B%i == 0:
		ans.append(i)
print(ans[len(ans)-K])

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

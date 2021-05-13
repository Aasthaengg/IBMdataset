import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

S = input()
ans = 0
st1 = ''
st2 = ''
for s in S:
	st2 += s
	if st2 != st1:
		ans += 1
		st1 = st2
		st2 = ''
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

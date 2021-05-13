import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(input())
for i in range(N, 1000):
	if i//100==(i//10)%10:
		if i//100==i%10:
			print(i)
			sys.exit()

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

K = int(input())
A, B = map(int, input().split())
for i in range(A, B+1):
	if i % K == 0:
		print('OK')
		sys.exit()
print('NG')

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

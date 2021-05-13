import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

A = inpl()
B = inpl()
if A[0] != B[0]:
    print(1)
else:
    print(0)

# -----------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

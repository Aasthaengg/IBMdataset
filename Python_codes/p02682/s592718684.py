import sys
read = sys.stdin.readline
import time
import math
import itertools as it
def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
start_time = time.perf_counter()
# ------------------------------

A, B, C, K = inpl()
xa = min(K, A)
K -= xa
xb = min(K, B)
K -= xb
xc = K
print(xa-xc)


# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)
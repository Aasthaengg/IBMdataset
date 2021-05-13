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

n = inp()
print(int((n-1)*n//2))

# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)
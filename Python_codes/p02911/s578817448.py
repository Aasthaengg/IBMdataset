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

n, k, q = inpl()
A = [inp()-1 for i in range(q)]
dp = [0] * n
for a in A:
    dp[a] += 1
cnt = 0
for i in dp:
    if k - q + i > 0:
        print('Yes')
    else:
        print('No')

# -----------------------------
end_time = time.perf_counter()
print('time:', end_time-start_time, file=sys.stderr)
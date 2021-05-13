import sys
import time
import math
import itertools as it
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N, M = inpl()
dp = [-1] * N
for _ in range(M):
    s, c = inpl()
    s -= 1
    if dp[s] not in [-1, c]:
        print(-1)
        sys.exit()
    dp[s] = c
for i in range(N):
    if N == 1:
        if dp[i] == -1:
            print(0, end='')
        else:
            print(dp[i], end='')
    else:
        if i == 0:
            if dp[i] == -1:
                print(1, end='')
            elif dp[i] == 0:
                print(-1)
                sys.exit()
            else:
                print(dp[i], end='')
        else:
            if dp[i] == -1:
                print(0, end='')
            else:
                print(dp[i], end='')
                
print()
# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)

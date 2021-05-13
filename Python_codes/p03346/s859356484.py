import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

cnt = [0] * (N + 1)

for i in P:
    if cnt[i - 1] != 0:
        cnt[i] = cnt[i-1] + 1
        cnt[i - 1] = 0
    else:
        cnt[i] = 1

print(N - max(cnt))

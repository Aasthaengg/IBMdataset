import sys
import numpy as np
from collections import defaultdict

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
A = np.array([0] + lr())
A = (A-1) % K
Acum = A.cumsum() % K
counter = defaultdict(int)
answer = 0
for i, x in enumerate(Acum):
    answer += counter[x]
    counter[x] += 1
    if i >= K-1:
        counter[Acum[i-(K-1)]] -= 1

print(answer)

import numpy as np
from collections import defaultdict

N, K = map(int, input().split())
A = np.array([0] + list(map(int, input().split())))

B = (np.add.accumulate(A) - np.arange(N+1)) % K

counter = defaultdict(int)
ans = 0

for j in range(N+1):
    if j - K >= 0:
        counter[B[j-K]] -= 1
    ans += counter[B[j]]
    counter[B[j]] += 1

print(ans)

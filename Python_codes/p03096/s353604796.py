import numpy as np
from collections import defaultdict
from operator import itemgetter
import sys

input = sys.stdin.readline

MOD = 10 ** 9 + 7


d = defaultdict(list)

N = int(input())
for i in range(N):
    C = int(input())
    d[C].append(i)

pairs = []
for c, indices in d.items():
    for i in range(len(indices) - 1):
        if indices[i+1] - indices[i] > 1:
            pairs.append((indices[i], indices[i+1]))

pairs.sort(key = itemgetter(1))   


dp = np.zeros(N, np.int64)
dp[0] = 1
index = 0
for i in range(1, N):
    dp[i] = dp[i-1]
    while index < len(pairs) and pairs[index][1] == i:
        dp[i] += dp[pairs[index][0]] 
        index += 1
    dp[i] %= MOD

print(dp[-1])
        



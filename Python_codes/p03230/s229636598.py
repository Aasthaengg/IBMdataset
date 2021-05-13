from itertools import combinations as cb
import sys

N = int(input())

k = (1 + int((1 + 8 * N) ** 0.5)) // 2

if k * (k - 1) // 2 != N:
    print('No')
    sys.exit()

print('Yes')
print(k)

x = list(cb(range(k), 2))
dp = [[] for i in range(k)]
for i,(a,b) in enumerate(x):
    dp[a].append(i+1)
    dp[b].append(i+1)
for r in dp:
    print(len(r), *r)
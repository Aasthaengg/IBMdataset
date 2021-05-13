from itertools import combinations
import sys
n, k = map(int, input().split())

if (n-1) * (n-2) // 2 < k:
    print(-1)
    sys.exit()

n_add  = (n-1) * (n-2) // 2 - k
print(n_add + n - 1)

for i in range(2, n+1):
    print(1, i)

for i, (v1, v2) in enumerate(combinations(range(2, n+1), 2)):
    if i == n_add:
        break
    print(v1, v2)

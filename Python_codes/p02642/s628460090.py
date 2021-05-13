import numpy as np
from collections import Counter


len_arr = int(input())
arr = list(map(int, input().split(' ')))
counter = Counter(arr)
x_max = max(counter.keys())

dp = np.empty(x_max+1, dtype=np.bool_)
dp[:] = True

ans = 0

for x, count in sorted(counter.items()):
    multi = [x*y for y in range(1, x_max//x+1)]
    if count == 1 and dp[x]:
        ans += 1
    dp[multi] = False

print(ans)

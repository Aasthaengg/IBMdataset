from collections import defaultdict
import numpy as np
import sys

n = int(input())
xy = np.array([list(map(int, input().split())) for _ in range(n)])

if n == 1:
    print(1)
    sys.exit()

memo = defaultdict(int)

for i in xy:
    for j in xy:
        if np.all(i == j):
            continue
        else:
            tmp = j - i
            if tmp[0] < 0:
                tmp *= -1
            elif tmp[0] == 0 and tmp[1] < 0:
                tmp *= -1
            memo[str(tmp)] += 1

print(n - max(memo.values()) // 2)
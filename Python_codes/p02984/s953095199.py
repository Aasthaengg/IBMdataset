import numpy as np
n = int(input())
arr = np.array(list(map(int, input().split())))

ans = np.zeros(n + 1, dtype=int)
for i, x in enumerate(arr):
    tmp = x * 2 - ans[i]
    ans[i + 1] += tmp

x = ans[-1] // 2
ans = ans[:-1]
ans[0::2] += x
ans[1::2] -= x

print(*ans)
import numpy as np

h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = []
for i, e in enumerate(a, 1):
    ans += [i] * e

ans = np.array(ans, dtype=np.int64)
ans = ans.reshape((h, w))

for i in range(1, h, 2):
    ans[i] = ans[i][::-1]

for ar in ans:
    print(*ar)

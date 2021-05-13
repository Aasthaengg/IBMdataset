import numpy as np

h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = []
for i, e in enumerate(a, 1):
    ans += [i] * e

ans = np.array(ans, dtype=np.int16)
ans = ans.reshape((h, w))

ans[1::2, :] = ans[1::2, ::-1]

for ar in ans:
    print(*ar)

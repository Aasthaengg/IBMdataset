import numpy as np

# 終点でソート
N, M = map(int, input().split())
AB = np.array([input().split() for _ in range(M)], np.int32)
AB = sorted(AB, key=lambda x: x[1])
ans, end = 0, 0
for a, b in AB:
    # print(end, a, b)
    if end <= a:
        ans += 1
        end = b
print(ans)

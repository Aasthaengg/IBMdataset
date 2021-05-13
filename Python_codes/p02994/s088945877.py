import numpy as np

N, L = map(int, input().split())
taste = [L + i for i in range(N)]
remove = np.argmin(np.abs(taste))
taste_sum = 0
for i in range(N):
    if i == remove:
        continue
    else:
        taste_sum += taste[i]
print(taste_sum)
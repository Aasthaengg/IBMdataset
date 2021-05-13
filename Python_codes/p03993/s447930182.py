import numpy as np
N = int(input())

a = list(map(int, input().split()))
a = np.array(a)
a = a - 1

cnt = 0

for i in range(N):
    if i == a[a[i]]:
        cnt += 1

print(cnt//2)

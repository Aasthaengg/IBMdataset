import numpy as np
N = int(input())
a = list(map(int, input().split()))

mean_a = np.mean(a)
cnt = 0
num = 0
for i in range(N):
    if abs(a[i] - mean_a) < abs(cnt - mean_a):
        cnt = a[i]
        num = i
print(num)

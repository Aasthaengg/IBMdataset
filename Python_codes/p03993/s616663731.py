import numpy as np
n = int(input())
a = list(map(int, input().split()))
a = np.array(a) - 1

ans = 0
for i in range(n):
    if a[a[i]] == i:
        ans += 1

print(ans // 2)

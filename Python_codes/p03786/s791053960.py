import numpy as np

N = int(input())
A = list(map(int, input().split()))
A.sort()
cumsum = np.cumsum(A)
ans = 1

for i in range(N - 2, -1, -1):
    if cumsum[i] * 2 >= A[i + 1]:
        ans += 1
    else:
        break

print(ans)

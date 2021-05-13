import numpy as np
n = int(input())
A = np.array(list(map(int, input().split())))
A -= 1

ans = 0
seen = [0] * n
for i, ai in enumerate(A):
    if seen[i]:
        continue
    seen[i] = 1
    if A[ai] == i:
        ans += 1
        seen[ai] = 1

print(ans)

import numpy as np

n, m, k = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

a = [0]
b = [0]

a = np.append(a, np.cumsum(A))
b = np.append(b, np.cumsum(B))

j = m
ans = 0
for i in range(n + 1):
    if a[i] > k:
        break
    while a[i] + b[j] > k:
        j -= 1
    ans = max(ans, i + j)
    
print(ans)
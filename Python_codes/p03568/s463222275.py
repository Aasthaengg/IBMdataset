import numpy as np

n = int(input())
a = list(map(int, input().split()))
a = np.array(a)

k = 1
for x in a:
    if x % 2 == 0:
        k *= 2

ans = pow(3, n) - k

print(ans)

import numpy as np
n = int(input())
al = sorted(list(map(int, input().split())))
c = list(np.cumsum(al))

ans = 1
for i in range(n-1):
    if c[i]*2 >= al[i+1]:
        ans += 1
    else:
        ans = 1

print(ans)

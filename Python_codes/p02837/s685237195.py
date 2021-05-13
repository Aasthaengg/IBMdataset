import numpy as np
import itertools
n = int(input())
ixy = []
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int, input().split())
        ixy.append([i,x-1,y])

ans = 0
ixy = np.array(ixy)
p = itertools.product([True,False], repeat=n)
for p_i in p:
    f = True
    for i,x,y in ixy:
        if not p_i[i]:
            continue
        else:
            if p_i[x] != y:
                f = False
                break
    if f:
        ans = max(sum(p_i), ans)
print(ans)
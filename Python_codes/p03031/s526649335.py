from itertools import product
from copy import deepcopy

n, m = map(int, input().split())
k = []
s = []
for j in range(m):
    a = list(map(int, input().split()))
    k.append(a[0])
    s.append(deepcopy(a[1:]))
p = list(map(int, input().split()))

ans = 0
for x in product([0,1], repeat=n):
    c = True
    for i in range(m):
        count = 0
        for j in range(k[i]):
            if x[s[i][j]-1] == 1:
                count += 1
        if count % 2 != p[i]:
            c = False
            break
    if c:
        ans += 1
print(ans)
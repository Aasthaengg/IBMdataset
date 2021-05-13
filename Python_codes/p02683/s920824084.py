import numpy as np

N, M, X = [int(x) for x in input().split()]

data = [[] for _ in range(N)]

for i in range(N):
    data[i] = [int(x) for x in input().split()]

ans = 12 * (10 ** 5) + 1
ok = False
for i in range(2 ** N):
    v = np.array([0] * (M + 1))
    for j in range(N):
        if (i >> j) & 1:
            v += np.array(data[j])
    x = min(list(v)[1:])
    if X <= x:
        ok = True
        ans = min(ans, v[0])

if ok == True:
    print(ans)
else:
    print(-1)
import numpy as np
N, M = map(int, input().split())
l = np.zeros((N, 2), dtype = int)
for i in range(M):
    p, S = map(str, input().split())
    if S == 'AC':
        l[int(p) - 1, 0] = 1
    elif S =='WA' and l[int(p) - 1, 0] == 1:
        continue
    else:
        l[int(p) - 1, 1] += 1
print(np.sum(l[:, 0]), np.sum(l[l[:, 0] == 1, 1]))
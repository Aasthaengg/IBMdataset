h, w, k = map(int, input().split())
c = [[] for _ in range(h)]
for i in range(h):
    c[i] = input()

res = 0
from itertools import product
for v1 in product([0,1], repeat=h):
    for v2 in product([0,1], repeat=w):
        cnt = 0
        for i in range(h):
            if v1[i] == 0: continue
            for j in range(w):
                if v2[j] == 1 and c[i][j] == '#':
                    cnt += 1
        if cnt == k:
            res += 1
print(res)
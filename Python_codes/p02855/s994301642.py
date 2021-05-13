H, W, K = map(int, input().split())
S = []

for _ in range(H):
    s = list(input())
    S.append(s)

ans = [[0 for wi in range(W)] for hi in range(H)]

from collections import defaultdict
found = defaultdict(list)
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            found[i].append(j)

cur = 1
for i in range(H):
    if i in found.keys():
        for j in range(W):
            ans[i][j] = cur
            if S[i][j] == '#':
                if found[i][-1] != j:
                    cur += 1
        cur += 1

foundp = list(found.keys())
foundp.sort()
kmax = foundp[-1]
kmin = foundp[0]
np = 0
for i in range(H):
    if i not in found.keys():
        if i < kmax:
            while not i < foundp[np]:
                np += 1
            ans[i] = ans[foundp[np]]
        else:
            ans[i] = ans[kmax]

for s in range(H):
    print(*ans[s])
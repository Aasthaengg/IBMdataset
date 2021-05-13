from itertools import permutations

N, C = map(int, input().split())
D = list()
for _ in range(C):
    D.append(list(map(int, input().split())))

c = list()
for _ in range(N):
    c.append(list(map(int, input().split())))

# sum of wrongnesses to repaint i-th strip to color j. (i=0,1,2,  j=0,1,...,C-1)
sw = [[0] * C for _ in range(3)]

for i in range(N):
    for j in range(N):
        idc = c[i][j] - 1
        for _idc in range(C):
            sw[(i + j) % 3][_idc] += D[idc][_idc]

ans = 10**9
for p in permutations(range(C), 3):
    tmp = 0
    for idx, q in enumerate(p):
        tmp += sw[idx][q]

    if ans > tmp:
        ans = tmp

print(ans)


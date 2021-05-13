import copy

h, w, k = map(int, input().split())
grd = [list(i for i in input()) for _ in range(h)]
ans = 0
for i in range(2**h):
    grd1 = copy.deepcopy(grd)
    for i1 in range(h):
        if i >> i1 & 1:
            grd1[i1] = ['r'] * w
    for j in range(2**w):
        grd2 = copy.deepcopy(grd1)
        for j1 in range(w):
            if j >> j1 & 1:
                for n in range(h):
                    grd2[n][j1] = 'r'

        if sum(grd2,[]).count('#') == k:
            ans += 1
print(ans)
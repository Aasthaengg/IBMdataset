from itertools import product

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for hl in product([0, 1], repeat=h):
    for wl in product([0, 1], repeat=w):
        cnt = 0
        for ci, hi in zip(c, hl):
            for cij, wj in zip(ci, wl):
                if hi == 0 and wj == 0:
                    cnt += (cij == '#')
        ans += (cnt == k)
print(ans)

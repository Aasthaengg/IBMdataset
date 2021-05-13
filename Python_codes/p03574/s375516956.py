hw, *ss = open(0).read().splitlines()

H, W = map(int, hw.split())

ss = list(map(list, ss))

from itertools import product

for h in range(H):
    for w in range(W):
        if ss[h][w] == '#':
            continue
        ans = 0
        for i,j in product([-1,0,1], [-1,0,1]):
            if 0 <= h+i < H and 0 <= w+j < W:
                ans += (ss[h+i][w+j] == '#')
        ss[h][w] = ans

for s in ss:
    print(''.join(map(str, s)))
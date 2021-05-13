# -*- coding: utf-8 -*-
D, G = map(int, input().split(' '))
p_c_pairs = [((i+1) * 100, list(map(int, input().split(' ')))) for i in range(D)]

import math
ans = float('inf')
p_c_pairs.sort(key=lambda x: -x[0])
for d in range(1<<D):
    # print(bin(d))

    cnt = 0
    g = G
    for i in range(D):
        if 1 & (d >> i):
            score, (p, c) = p_c_pairs[i]
            g -= score * p + c
            cnt += p

    if g > 0:
        for i in range(D):
            if not (1 & (d >> i)):
                score, (p, c) = p_c_pairs[i]
                n = min(p, int(math.ceil(g/score)))
                g -= score * n
                cnt += n
                break

    # print(bin(d), g)
    if g <= 0:
        ans = min(ans, cnt)

print(ans)
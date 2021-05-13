# -*- coding: utf-8 -*-
H, W = map(int, input().split(' '))
table = [list(map(int, input().split(' '))) for _ in range(H)]

def get_next():
    for h in range(H):
        if h % 2:
            for w in range(W-1, -1, -1):
                yield h, w
        else:
            for w in range(W):
                yield h, w


ret = []
routes = list(get_next())
prv_h, prv_w = routes[0]
for h, w in routes[1:]:
    if table[prv_h][prv_w] % 2:
        ret.append((prv_h, prv_w, h, w))
        table[h][w] += 1

    prv_h, prv_w = h, w


print(len(ret))
for prv_h, prv_w, h, w in ret:
    print(prv_h + 1, prv_w + 1, h + 1, w + 1)





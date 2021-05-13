# -*- coding: utf-8 -*-
H, W, A, B = map(int, input().split(' '))
row1 = [1 for _ in range(A)] + [0 for _ in range(W-A)]
row2 = [0 for _ in range(A)] + [1 for _ in range(W-A)]

table = [list(row1) for _ in range(B)] + [list(row2) for _ in range(H - B)]
for row in table:
    print(''.join(map(str, row)))






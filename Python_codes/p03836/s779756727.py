# -*- coding: utf-8 -*-
sx, sy, tx, ty = map(int, input().split())
dx,dy = tx-sx, ty-sy

r1 = 'U'*dy + 'R'*dx
r2 = 'D'*dy + 'L'*dx

r3 = 'LU'+r1+'RD'
r4 = 'RD'+r2+'LU'

print(r1+r2+r3+r4)
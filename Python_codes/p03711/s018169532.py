# -*- coding: utf-8 -*-

x, y = map(int, input().split())

g= {1:'g1', 2:'g3', 3:'g1', 4:'g2', 5:'g1', 6:'g2', 7:'g1', 8:'g1', 9:'g2', 10:'g1', 11:'g2', 12:'g1'}

if g[x] == g[y]:
    print('Yes')
else:
    print('No')
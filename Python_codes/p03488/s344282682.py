# -*- coding: utf-8 -*-
import sys
from itertools import product
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
S = readline().decode().rstrip()
x,y = map(int,readline().split())
L = [len(i) for i in S.split('T')]
x -= L[0]
X = L[2::2]
Y = L[1::2]

dx = {0}
dy = {0}

for i in X:
    dx = {x+j for x,j in product(dx,[i,-i])}
for i in Y:
    dy = {y+j for y,j in product(dy,[i,-i])}

if x in dx and y in dy:
    print('Yes')
else:
    print('No')
# -*- coding: utf-8 -*-
#D - Static Sushi 
import sys 
from math import sqrt
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())

M = 55555
p = [1]*(M+1)
p[0] = p[1] = 0
### エラストネスのふるい
for x in range(2, int(sqrt(M))+1):
    if p[x]:
        for y in range(x*x, M+1, x):
            p[y] = 0

## Mまでの5a+1を満たす素数の集合P
P = []
cnt = 0
for i in range(1,M+1):
    if p[i] and (i-1) % 5 == 0:
        P.append(i)

print(*P[:N])
#coding: utf-8
from collections import deque

H, W = (int(x) for x in input().split())
A = []

curMove = []
moves = []
hasOdd = False
pi = -1
pj = -1
for i in range(H):
    row = [int(x) for x in input().split()]
    if i % 2 == 0:
        start, end, diff = 0, W, 1
    else:
        start, end, diff = W-1, 0-1, -1

    for j in range(start, end, diff):
        if row[j] % 2 == 1:
            if hasOdd:
                curMove.append((pi,pj, i, j))
                moves += curMove
                curMove = []
                hasOdd = False
            else:
                hasOdd = True
        else:
            if hasOdd:
                curMove.append((pi,pj, i, j))
        pi = i
        pj = j

print(len(moves))
for m in moves:
    print(" ".join((str(i+1) for i in m)))

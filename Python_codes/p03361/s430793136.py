__DEUBG__ = 0

import math
import sys

H, W = map(int, input().split())

board = [
  list(input())
  for _ in range(H)]

def calc(board, x, y):
    if board[x][y] == '#':
        for i,j in [
          (x, y-1),
          (x-1, y),
          (x+1, y),
          (x, y+1)
        ]:
            if 0 <= i <= H-1 and 0 <= j <= W-1:
                if board[i][j] == '#':
                    return
        print('No')
        exit()
    else:
        return

for i in range(H):
    for j in range(W):
        if __DEUBG__:
            print(i, j)
        calc(board, i, j)

print('Yes')
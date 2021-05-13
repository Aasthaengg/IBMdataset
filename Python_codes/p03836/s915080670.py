#!/usr/bin/env python3
# coding:utf-8

def main():
    sx, sy, tx, ty = map(int, input().split())
    stdOut = solve(sx, sy, tx, ty)
    print(stdOut)

"""
方針
sx < tx , sy < tyなので
進路としては
1sx,syから右にtx,syまで移動後上にtx,tyまで移動
2tx,tyから左にsx,tyまで移動後下にsx,syまで移動
3下に1移動、右にtx+1,sy-1まで移動、上にtx+1,tyまで移動、左に1移動
4上に1移動、左にsx-1,ty+1まで移動、下にsx-1,syまで移動、右に1移動

"""

up = 'U'
down = 'D'
left = 'L'
right = 'R'

def solve(sx, sy, tx, ty):
    deltax = tx - sx
    deltay = ty - sy
    movelog = ''
    movelog += up * deltay + right * deltax
    movelog += down * deltay + left * deltax
    movelog += down + right * (deltax + 1) + up * (deltay + 1) + left
    movelog += up + left * (deltax + 1) + down * (deltay + 1) + right

    return movelog

if __name__ == "__main__":
    main()

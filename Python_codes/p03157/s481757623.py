from fractions import gcd
# from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
import sys
from bisect import *
import itertools
import copy
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7

#グリッドを適当に移動してみると、いくつかの連結成分ができる
#その連結成分の条件を満たす組は（白の個数）×(黒の個数)で求まる。
#あとはそれを、すべての連結成分毎に足し合わせる
#PyPyは再帰遅い
def main():
    
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    start = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#": 
                start.append([i,j])

    ans = [0,0]
    vis = [[-1 for i in range(w)] for j in range(h)]
    def f(x, y, pre):
        vis[x][y] = 1
        if s[x][y] == "#":
            ans[0] += 1
        else:
            ans[1] +=1
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = i + x
            ny = j + y
            if nx >= 0 and ny >= 0 and nx < h and ny < w and vis[nx][ny] == -1:
                if pre == "B" and s[nx][ny] == ".":
                    f(nx,ny,"W")
                elif pre == "W" and s[nx][ny] == "#":
                    f(nx, ny, "B")
                
    
    ret = 0
    for i, j in start:
        if vis[i][j] == -1:
            f(i, j, "B")
        ret += ans[0] * ans[1]
        ans[0] = ans[1] = 0
    print(ret)
        

if __name__ == '__main__':
    main()

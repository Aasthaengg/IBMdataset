import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    h,w = map(int, input().split())
    s = [input().rstrip() for i in range(h)]

    visited = [[0]*w for i in range(h)]
    dist = [[INF]*w for i in range(h)]

    que = deque([(0,0)])
    visited[0][0] = 1
    dist[0][0] = 0

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    while len(que) > 0:
        x,y = que.popleft()
        if x == w-1 and y == h-1: # ゴールまで辿ったら
            break

        for k in range(4): # 上下左右4パターンの移動方法
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<w and 0<=ny<h and s[ny][nx]=='.' and visited[ny][nx]==0:
                que.append((nx,ny))
                visited[ny][nx] = 1
                dist[ny][nx] = dist[y][x] + 1

    if dist[h-1][w-1] == INF:
        print(-1)
    else:
        print(sum(s[i].count(".") for i in range(h)) - (dist[h-1][w-1]+1))


if __name__=="__main__":
    main(
    )

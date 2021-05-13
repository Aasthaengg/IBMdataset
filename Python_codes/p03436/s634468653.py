import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    R,C = NMI()
    sy, sx = 0,0
    gy, gx = R-1,C-1
    board = [list(input()) for _ in range(R)]

    #移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #すべての点をINFで初期化
    INF = R*C*2
    distance = [[INF for _ in range(C)] for _ in range(R)]

    #地点を保存するqueを作成、スタート地点を入れる
    que = deque([])
    que.append((sy,sx))

    #スタート地点の距離は0
    distance[sy][sx] = 0
    
    #最短経路
    shortest = INF

    #queが空になるまでループ
    while len(que) != 0:
        #取り出してきた状態がゴールなら探索をやめる
        pop = que.popleft()
        if pop[0]==gy and pop[1]==gx:
            shortest = distance[gy][gx]+1


        #移動4方向をループ
        for i in range(len(dx)):
            #移動した後の点をny,nxとする
            ny = pop[0]+dy[i]
            nx = pop[1]+dx[i]

            #nyが0以上R未満   nxが0以上C未満     盤上で壁ではない        まだ訪れたことがない
            if 0<= ny < R and 0 <= nx < C and board[ny][nx]!='#' and distance[ny][nx] == INF:
                #つまり移動可能でまだ行ったことがなければqueへ入れる
                que.append((ny,nx))
                #その距離をもとのpopの最短距離+1でdistanceに記録
                distance[ny][nx] = distance[pop[0]][pop[1]]+1
    
    if shortest == INF:
        print(-1)
    else:
        dots = 0
        for r in range(R):
            for c in range(C):
                if board[r][c] == '.':
                    dots += 1
        print(dots-shortest)

if __name__ == '__main__':
    main()
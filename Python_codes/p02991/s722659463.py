#!/usr/bin/env python3
#ABC132 E
#有向グラフ上の路長が3の倍数であるようなものの内、最短の長さを3で割ったものを出力

import sys
sys.setrecursionlimit(1000000)
from collections import deque

N,M = map(int,input().split())
UV = [list(map(int,input().split())) for _ in range(M)]
S,T = map(int,input().split())

G = [[] for _ in range(N)]

for i in UV:
    G[i[0]-1].append(i[1]-1)

reach = [[-1 for _ in range(N)] for _ in range(3)]#元のグラフのGの状態数3倍化
reach[0][S-1] = 0#スタート位置を0にする

que = deque()
que.append(S-1)#スタート位置を追加

time = 1
for _ in range(4*N):
    new_que = deque()
    for q in que:
        for v in G[q]:#qから移動できる辺を見る
            if reach[time%3][v] == -1:#まだたどり着いていない辺なら
                reach[time%3][v] = time#たどり着けた時刻をたどり着いた時刻を3で割った余りのリストに入れる
                new_que.append(v)#たどり着いた頂点をqueueにいれて次のターンでそこから移動できる辺を見る
    que = new_que
    time += 1
if reach[0][T-1] == -1:
    print(-1)
else:
    print(reach[0][T-1]//3)

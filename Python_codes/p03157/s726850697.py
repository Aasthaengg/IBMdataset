#!/usr/bin python3
# -*- coding: utf-8 -*-

H, W = map(int,input().split())

INF = -1
Gmap = [list(input()) for _ in range(H)]
Seen = [[INF]*W for _ in range(H)]
direc = {(1,0), (-1,0), (0,1), (0,-1)}
init_q =[]

from collections import deque

def bfs(sth, stw):
    black = 1
    white = 0
    next_q = deque([])
    next_q.append((sth, stw))
    while len(next_q)!=0:
        #キュー取り出し(先頭)
        h, w = next_q.popleft()
        Seen[h][w] = 0
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<H and 0<=ws<W):
                continue
            if Gmap[h][w]=='#' and Gmap[hs][ws]=='.' and Seen[hs][ws]==INF:
                Seen[hs][ws]=0
                next_q.append((hs, ws))
                white +=1
            if Gmap[h][w]=='.' and Gmap[hs][ws]=='#' and Seen[hs][ws]==INF:
                Seen[hs][ws]=0
                next_q.append((hs, ws))
                black +=1
#        print(black,white)
    return black * white

#複数
ret = 0
for sth in range(H):
    for stw in range(W):
        if Gmap[sth][stw]=='#' and Seen[sth][stw]==INF:
            x = bfs(sth, stw)
#                print(sth,stw ,x)
            ret += x
print(ret)

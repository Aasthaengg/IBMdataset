#!/usr/bin python3
# -*- coding: utf-8 -*-

H, W = map(int,input().split())
sth, stw = 0, 0
glh, glw = H-1, W-1

INF = 0
Gmap = [list(input()) for _ in range(H)]
Dist = [[INF]*W for _ in range(H)]
direc = {(1,0), (0,1)}
mod = 10**9+7

from collections import deque

def bfs(init):
    next_q = deque([])
    for hi, hw in init:
        next_q.append([hi,hw])
        Dist[hi][hw] = 1

    while len(next_q)!=0:
        #キュー取り出し(先頭)
        h,w = next_q.popleft()
        for d in direc:
            hs, ws = h + d[0], w + d[1]
            if not (0<=hs<H and 0<=ws<W):
                continue
            if Gmap[hs][ws]=='.':
                if Dist[hs][ws]==INF:
                    next_q.append([hs,ws])
                Dist[hs][ws] += Dist[h][w]
                Dist[hs][ws] %= mod
    return Dist

def main():
    ret = bfs([[sth, stw]])
    print(ret[glh][glw])

if __name__ == '__main__':
    main()
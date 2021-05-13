# -*- coding: utf-8 -*-
#重み付きUnion-Findによる実装
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        px = find(par[x])
        wei[x] += wei[par[x]]
        par[x] = px
        return px

#xの根から距離
def weight(x):
    find(x)
    return wei[x]


#w[y]=w[x]+wとなるようにxとyを併合
def unite(x,y,w):
    w += wei[x]-wei[y]
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
            w = -w
        par[x] += par[y]
        par[y] = x
        wei[y] = w
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#x,yが同じ集合に属するときのwei[y]-wei[x]
def diff(x,y):
    return weight(y)-weight(x)

N,M = map(int,readline().split())
#0-index
par = [-1]*N
wei = [0]*N
for _ in range(M):
    l,r,d = map(int,readline().split())
    l,r = l-1,r-1
    if same(l,r):
        if d != diff(l,r):
            print('No')
            exit()
    else:
        unite(l,r,d)
print('Yes')
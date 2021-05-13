# -*- coding: utf-8 -*-
import sys 
from collections import defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#Union Find

#xの根を求める
def find(x,par):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x],par)
        return par[x]
#xとyの属する集合の併合
def union(x,y,par):
    x = find(x,par)
    y = find(y,par)
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y] #xにyの個数くっつける 
        par[y] = x #yをxにくっつける
        return True

#xとyが同じ集合に属するかの判定
def same(x,y,par):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

N,K,L = map(int,readline().split())
par_road = [-1]*(N+1)
par_rail = [-1]*(N+1)


for i in range(K):
    x,y = map(int,readline().split())
    union(x,y,par_road)
    
for i in range(L):
    x,y = map(int,readline().split())
    union(x,y,par_rail)
    
num = []
d = defaultdict(int)  
for i in range(1,N+1):
    id = find(i,par_road)+find(i,par_rail)*10**6
    num.append(id)
    d[id] += 1

print(' '.join(str(d[n]) for n in num))

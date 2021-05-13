#!/usr/bin/env python3
#写経
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#　縦に並んだ入力を受け取りたい時はread().split()をとる zip(m,m)で分ける
N,U,V = map(int,readline().split())
m = map(int,read().split())
AB = zip(m,m)

#tree の受け取り：頂点の数＋１のリストを用意して、それぞれの頂点が辺を貼るnodeを全てリストに保存
graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)
#全探索して入力頂点からの距離を返す
#全ての頂点に対して、
def dfs(v):
    dist = [-1] * (N+1)
    stack = [v]
    dist[v] = 0
    while stack:
        v = stack.pop()
        dw = dist[v] + 1
        for w in graph[v]:#頂点から辺が貼られている頂点に対して
            if dist[w] >= 0:#すでに訪れている
                continue
            dist[w] = dw#訪れてないなら更新
            stack.append(w)
    return dist

DU,DV = dfs(U),dfs(V)
 
answer = 0
#元の場所以外の全ての頂点を探索する
for u,v in zip(DU[1:],DV[1:]):
    if u < v:#逃げる方が先につく中で最短を探す
        x = v - 1
        if answer < x:
            answer = x
 
print(answer)
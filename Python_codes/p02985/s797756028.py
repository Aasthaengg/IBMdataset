# -*- coding: utf-8 -*-
import sys
from collections import deque
N,K=map(int, sys.stdin.readline().split())

al=[ [] for _ in range(N+1) ]	#隣接リスト
for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    al[a].append(b)
    al[b].append(a)
   
mod=10**9+7
ans=1

#dfs
start=1
Visit=[ 0 for _ in range(N+1) ] #訪問した頂点
q=deque()
q.append((start,K)) #(現在位置、使用できる色の数)
Visit[start]=1

while q:
    fro,k=q.pop()
    ans*=k  #答えに使用できる色の通り数をかける
    ans%=mod
    if fro==1:  #ルートノードの時は
        num=K-1
    else:       #ルートノードじゃない時は
        num=K-2  #K-2色使用できる
    for to in al[fro]:
        if Visit[to]==0:
            Visit[to]=1	#訪問済みVisitに1をセットする。4行上のpopleftの直後でVisitをセットすると同じ頂点がqに入り、TLEする
            q.append((to,num))
            num-=1
print ans
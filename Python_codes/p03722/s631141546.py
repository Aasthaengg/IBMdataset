# -*- coding: utf-8 -*-
import sys
from collections import deque

N,M=map(int, sys.stdin.readline().split())
al=[ [] for _ in range(N+1) ]   #隣接リスト
rev_al=[ [] for _ in range(N+1) ]   #戻りを調べる用の隣接リスト
edge=[] #辺の集合
for _ in range(M):
    a,b,c=map(int, sys.stdin.readline().split())
    al[a].append(b)
    rev_al[b].append(a) #逆向きにも辺を張る
    edge.append((a,b,c))


go=[0 for _ in range(N+1)]
back=[0 for _ in range(N+1)]

#頂点１からNに行くまでに使用する頂点を調べる
q=deque()
q.append(1) #スタート地点
go[1]=1

while q:
    fro=q.popleft()
    for to in al[fro]:
        if go[to]==0:
            go[to]=1
            q.append(to)


#頂点Nから1に戻る際に使用する頂点を調べる
q=deque()
q.append(N) #スタート地点
back[N]=1

while q:
    fro=q.popleft()
    for to in rev_al[fro]:
        if back[to]==0:
            back[to]=1
            q.append(to)


new_edge=[]     #有効な辺のみ抽出

for a,b,c in edge:
    if go[a]==1 and back[b]==1:
        new_edge.append((a,b,c))


#ベルマンフォード
dp=[ float("-inf") for _ in range(N+1) ]
dp[1]=0

for i in range(N):
    for fro,to,cost in new_edge:
        alt=dp[fro]+cost
        if dp[to]<alt:
            if i==N-1:
                print float("inf")
                quit()
            dp[to]=alt

print dp[N]
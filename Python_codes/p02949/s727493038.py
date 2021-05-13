#ABC137-D
# -*- coding: utf-8 -*-
import sys
from collections import deque

N,M,P=map(int, sys.stdin.readline().split())

al=[ [] for i in range(N+1) ]		#隣接リスト
rev_al=[ [] for i in range(N+1) ]	#reverse隣接リスト
#辺のリスト
edge=[]

for i in range(M):
	a,b,c=map(int, sys.stdin.readline().split())
	al[a].append(b)
	rev_al[b].append(a)
	edge.append((a,b,c-P))


#ゴールからBFS
#訪問した頂点
Visit=[ 0 for _ in range(N+1) ]
q=deque()
q.append(N)
Visit[N]=1
while q:
	fro=q.popleft()
	for to in rev_al[fro]:
		if Visit[to]==0:
			Visit[to]=1
			q.append(to)
			
Visit1=Visit

#スタートからBFS
#訪問した頂点
Visit=[ 0 for _ in range(N+1) ]
q=deque()
q.append(1)
Visit[1]=1
while q:
	fro=q.popleft()
	for to in al[fro]:
		if Visit[to]==0:
			Visit[to]=1
			q.append(to)

Visit2=Visit

#1からもNからも到達可能な頂点の集合
V=[]
for v1,v2 in zip(Visit1,Visit2):
	V.append(v1&v2)

new_N=sum(V)

fedge=[]	#必要な要素だけをフィルターした辺集合
for a,b,c in edge:
	if V[a]==1 and V[b]==1:
		fedge.append((a,b,c))


D=[ float("-inf") ]*(N+1)	#頂点１からの距離 1-indexed
D[1]=0

#Bellman-Ford
for i in range(new_N):
	for a,b,c in fedge:
		if D[a]==float("-inf"): continue
		alt=D[a]+c
		if D[b]<alt:
			D[b]=alt
			if i==new_N-1:
				print -1
				quit()

print max(0,D[N])
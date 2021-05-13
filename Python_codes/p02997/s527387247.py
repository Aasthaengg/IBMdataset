# -*- coding: utf-8 -*-
import sys
import itertools
N,K=map(int, sys.stdin.readline().split())
cnt=(N-1)*(N-2)/2 #距離2の組み合わせができる最大の通り数
if cnt<K:
    print -1
    quit()
L=list( itertools.combinations(range(1,N+1),2) )

M=N-1+cnt-K
print M
for i in range(N-1):
    print L[i][0],L[i][1]

for i in range(N-1,N-1+cnt-K):
    print L[i][0],L[i][1]

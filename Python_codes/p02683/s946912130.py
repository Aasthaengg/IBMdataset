# -*- coding: utf-8 -*-
import sys
N,M,X=map(int, sys.stdin.readline().split())
CA=[ map(int, sys.stdin.readline().split()) for _ in range(N) ]

ans=float("inf")

for n in range(2**N):
    #先頭列が金額、後は各アルゴリズムの理解度の合計値
    L=[ 0 for _ in range(M+1) ]
    for keta in range(N):
        if n%2==1:
            for i,t in enumerate(CA[keta]):
                L[i]+=t
        n/=2
        if X<=min(L[1:]):
            ans=min(ans,L[0])

if ans==float("inf"):
    print -1
else:   
    print ans
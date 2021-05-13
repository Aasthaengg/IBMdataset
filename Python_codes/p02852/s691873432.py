# -*- coding: utf-8 -*-
import sys

N,M=map(int, sys.stdin.readline().split())
S=sys.stdin.readline().strip()

L=[]    #答えの配列の逆順
for _ in range(N):
    for m in range(M,0,-1):
        if 0<=N-m and S[N-m]=="0":
            L.append(m)
            N-=m
            break
    else:
        break
        
if N!=0:
    print -1
else:
    print " ".join(map(str,L[::-1]))

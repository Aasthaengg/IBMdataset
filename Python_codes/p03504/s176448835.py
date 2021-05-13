# -*- coding: utf-8 -*-
import sys
from collections import deque

N,C=map(int, sys.stdin.readline().split()) 
stc=[ map(int, sys.stdin.readline().split()) for _ in range(N)]
stc.sort(key=lambda x:(x[0]) )
max_t=max(stc, key=(lambda x: x[1]))[1]

channel=[ deque() for _ in range(C+1) ]

for s,t,c in stc:
    try:
        prev_s,prev_t=channel[c].pop()
        if prev_t==s:
            channel[c].append((prev_s,t))
        else:
            channel[c].append((prev_s,prev_t))
            channel[c].append((s,t))
    except:
        channel[c].append((s,t))


T=[ 0 for _ in range(max_t+1) ] #時間軸

c=1
for c in range(1,C+1):  #チャンネル
    while channel[c]:
        s,t=channel[c].pop()
        for i in range(s,t+1):
            T[i]+=1

print max(T)

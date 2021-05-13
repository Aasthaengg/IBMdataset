# -*- coding: utf-8 -*-
import sys
from itertools import accumulate
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,c = map(int,readline().split())
stc = []
for i in range(n):
    stc.append(list(map(int,readline().split())))
stc.sort(key=lambda x: (x[2], x[0]))
 
nstc = []
for i in range(n):
    if len(nstc) > 0 and nstc[-1][2] == stc[i][2] and nstc[-1][1] == stc[i][0]: #同じチャンネルかつ終了時刻と始まりの時刻が同じ
        nstc[-1][1] = stc[i][1]
    else:
        nstc.append(stc[i])
n = len(nstc)
 
h = [0]*200005
for i in range(n):
    h[2*nstc[i][0] - 1] += 1
    h[2*nstc[i][1]] += -1
ah = list(accumulate(h))
print(max(ah))
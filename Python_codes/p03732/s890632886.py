# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n,W = [int(i) for i in readline().split()]
wv = [[int(i) for i in readline().split()] for j in range(n)]

w0 = wv[0][0]

d = [[] for i in range(4)]
for w,v in wv:
    d[w-w0].append(v)

from itertools import accumulate
ac = [None]*4
for i in range(4):
    d[i].sort(reverse=True)
    ac[i] = list(accumulate([0]+d[i]))

#print(d)
#print(ac)

ans = 0
di = len(ac[0])
dj = len(ac[1]) 
dk = len(ac[2]) 
dl = len(ac[3])

ac3 = ac[3]
for i in range(di):
    for j in range(min(n+1-i,dj)):
        for k in range(min(n+1-i-j,dk)):
            Wres = i*w0 + j*(w0+1) + k*(w0+2)
            if Wres > W: continue

            res = ac[0][i] + ac[1][j] + ac[2][k]
            idx = (W-Wres)//(w0+3)
            res += ac3[min(dl-1,idx)]
            if ans < res:
                ans = res

print(ans)            









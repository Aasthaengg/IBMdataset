# -*- coding: utf-8 -*-
#D - AtCoder Express 2
#2次元累積和
import sys 
from itertools import accumulate 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,M,Q = map(int,readline().split())
data = [[0]*(N+1) for _ in range(N+1)]
#入力
for _ in range(M):
    l,r = map(int,readline().split())
    data[l][r] += 1
    
#累積和
for i in range(N+1):
    for j in range(N):
        data[i][j+1] += data[i][j]
        
#入力    
for _ in range(Q):
    p,q = map(int,readline().split())
    ans = 0
    for i in range(p,q+1):
        ans += (data[i][q] - data[i][p-1])
    print(ans)
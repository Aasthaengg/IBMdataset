# -*- coding: utf-8 -*-
import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 998244353
N, S = map(int, readline().split())
A = list(map(int,readline().split()))

U = 3010
f = np.zeros(U,np.int64)
f[0] = 1
for a in A:
    ff = 2*f
    ff[a:] += f[:-a]
    ff%=MOD
    f = ff
ans = f[S]
print(ans%MOD)
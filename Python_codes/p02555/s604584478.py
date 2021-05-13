# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
S = int(readline())
f = [0]*2001
f[0] = 1
for i in range(3,S+1):
    f[i] = (f[i-1] + f[i-3]) % MOD
print(f[S])
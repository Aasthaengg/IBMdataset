# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 998244353
N, K = map(int, readline().split())
data = []
for _ in range(K):
    L,R = map(int, readline().split())
    data.append((L,R))
    
A = [0]*(N+1)
A[1] = 1
S = [0]*(N+1)
S[1] = 1

for i in range(2,N+1):
    for k in range(K):
        L,R = data[k]
        A[i] += (S[max(0,i-L)]- S[max(0,i-R-1)]) % MOD
        A[i] %= MOD
    S[i] = (S[i-1] + A[i]) % MOD

print(A[N])
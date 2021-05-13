# coding: utf-8

N, K, S = map(int,input().split())
if S == 10**9:
    A = [str(S-1)] * (N-K) + [str(S)] * K
else:
    A = [str(S+1)] * (N-K) + [str(S)] * K

print(' '.join(A))
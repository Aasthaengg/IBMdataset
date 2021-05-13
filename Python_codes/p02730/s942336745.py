# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
S = readline().decode().rstrip()
N = len(S)
half = N // 2
for i in range(half):
    if S[i] != S[-(i+1)]:
        print('No')
        sys.exit()
SS = S[:half]
for i in range(half//2):
    if SS[i] != SS[-(i+1)]:
        print('No')
        sys.exit()
print('Yes')
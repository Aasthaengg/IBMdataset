#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

S = input()
S = S + 'R'  # 下のループで最後の一回の加算を行う

A = [0] * len(S)

# 十分大きな(最大の連続するRかLの長さ程度<10**5)偶数回後には、RLと連続する箇所以外は全て0になる

conf = 0
even, odd = 0, 0
for i in range(len(S)-1):
    if i % 2:
        odd += 1
    else:
        even += 1

    if S[i+1] != S[i] and S[i] == 'R':
        conf = i
        if conf % 2:
            A[conf] += odd
            A[conf+1] += even
        else:
            A[conf] += even
            A[conf+1] += odd
        even, odd = 0, 0

    if S[i+1] != S[i] and S[i] == 'L':
        if conf % 2:
            A[conf] += odd
            A[conf+1] += even
        else:
            A[conf] += even
            A[conf+1] += odd
        even, odd = 0, 0


A = [str(i) for i in A[:-1]]
res = " ".join(A)
print(res)

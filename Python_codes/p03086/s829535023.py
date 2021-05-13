#!/usr/bin/python3
#coding: utf-8

S = input()

N = len(S)

ret = 0
for i in range(N):
    for j in range(i, N):
        sub = S[i:j+1]
        if all(c in ('A', 'C', 'G', 'T') for c in sub):
            ret = max(ret, len(sub))

print(ret)
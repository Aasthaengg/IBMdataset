import os, sys, re, math

N,K = list(map(int,input().split(' ')))
A = list(map(int,input().split(' ')))

d = math.ceil(math.log2(1e+12))
ones = [0 for _ in range(d)]

for a in A:
    s = bin(a)[::-1]
    for i in range(len(s)-2):
        if s[i] == '1':
            ones[i] += 1

X = 0
for di in range(d-1,-1,-1):
    if X + 2 ** di <= K and ones[di] <= N * 0.5:
        X += 2 ** di

ret = 0
for a in A:
    ret += X ^ a

print(ret)

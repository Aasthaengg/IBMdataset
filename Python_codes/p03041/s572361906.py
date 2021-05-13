#!/usr/bin/env python

N,K = list(map(int, input().split()))
S = input()

kmj = chr(ord(S[K-1])+32)

T = ""
for i in range(N):
    if i == K-1:
        T+=kmj
    else :
        T+=S[i]

print(T)
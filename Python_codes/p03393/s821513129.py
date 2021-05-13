#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()
#= map(int, input().split())
#= list(map(int, input().split()))
#= [input(), input()]
#= [list(map(int, input().split())) for _ in range(N)]
#= [int(input()) for _ in range(N)]
#= {i:[] for i in range(N)}

abc = "abcdefghijklmnopqrstuvwxyz"
dic = {d: 0 for d in abc}

for s in S:
    dic[s] += 1

for k in dic:
    if dic[k] == 0:
        print(S + k)
        exit()

li = []
for i in range(1, len(S) + 1):
    s = S[-i]
    for l in li:
        if s < l:
            print(S[: len(S) - i] + l)
            exit()
    li.append(s)
    li.sort()

print(-1)
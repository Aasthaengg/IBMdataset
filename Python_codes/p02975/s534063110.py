#!/usr/bin/env python3

#import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))
n = N // 3
dic = {}

for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

ans = True

if len(dic) > 3:
    ans = False

elif len(dic) == 3:
    keys = dic.keys()
    t = []
    for k in keys:
        t.append(k)
        if dic[k] != n:
            ans = False

    a = t[0]
    b = t[1]
    c = t[2]

    if (a ^ b) != c:
        ans = False

elif len(dic) == 2:
    for k in dic:
        if k == 0:
            if dic[k] != n:
                ans = False
        else:
            if dic[k] != n * 2:
                ans = False

else:
    keys = dic.keys()
    if not 0 in keys:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
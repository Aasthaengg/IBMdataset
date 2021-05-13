# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:53:14 2020

@author: liang
"""

S = input()

ans = S[0]

for i in range(8):
    tmp = int(S[0])
    lis = list()
    for j in range(3):
        lis.append(i>>j&1)
    for i in range(3):
        if lis[i] == 1:
            tmp += int(S[i+1])
        else:
            tmp -= int(S[i+1])
    #print(tmp)
    if tmp == 7:
        for i in range(3):
            if lis[i] == 1:
                ans += "+" + S[i+1]
            else:
                ans += "-" + S[i+1]
        ans += "=7"
        break
    #print(lis)
else:
    print("err")
print(ans)
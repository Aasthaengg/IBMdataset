# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:52:40 2020

@author: naoki
"""

N = int(input()) # 並んでいる人数N

S = input() # 向いている方向
    
change = [0 for i in range(N)] # 向きを変えた回数を格納
change[0] = S.count("E",1,N)
for i in range(1,N):
        if S[i-1] == "W" and S[i] == "E":
            change[i] = change[i-1]
        elif S[i-1] == "W" and S[i] != "E": 
            change[i] = change[i-1] + 1
        elif S[i-1] != "W" and S[i] == "E":
            change[i] = change[i-1] - 1
        else:
            change[i] = change[i-1]
change.sort()
print(change[0])
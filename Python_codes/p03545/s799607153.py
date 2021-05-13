# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:12:36 2020

@author: liang
"""

"""
eval関数
入力 :　式
    eval("2+3")
出力 : 値
    5
"""
S = input()

ans = S[0]
for i in range(8):
    tmp = S[0]
    
    for j in range(3):
        if i>>j&1 == 1:
            tmp += "+" + S[j+1]
        else:
            tmp += "-" + S[j+1]
    #print(tmp)
    #print(eval(tmp))
    if eval(tmp) == 7:
        #print("ok")
        ans = tmp
        ans += "=7"
        #print(ans)
        break
print(ans)
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:02:39 2020

@author: naoki
"""

a,b,x = map(int,input().split()) # 整数a,b及び割る数xを入力
if a!=0:
    print((b//x+1) - ((a-1)//x+1))
else:
    print(b//x + 1)
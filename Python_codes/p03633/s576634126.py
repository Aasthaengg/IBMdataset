# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:29:28 2020

@author: naoki
"""
import fractions

N = int(input()) # 時計の個数
T = [int(input()) for i in range(N)] # 時計の針が一周する時間
T.sort() # 小さい順番にソートする
lcm = T[0] 

for i in range(1,N):
    lcm = lcm*T[i]// fractions.gcd(lcm,T[i])
print(lcm)


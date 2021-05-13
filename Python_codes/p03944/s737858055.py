# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:09:47 2020

@author: sd18016
"""   

import sys

W, H, N = map(int, input().split())
list_x = []

for i in range(N):
    x = list(map(int, input().split()))
    list_x.append(x)
    
O = [0,0]
MU = [W, H]

for i in range(N):
    if list_x[i][2] == 1:
        if list_x[i][0] > O[0]:
            O[0] = list_x[i][0]
    elif list_x[i][2] == 2:
        if list_x[i][0] < MU[0]:
            MU[0] = list_x[i][0]
    elif list_x[i][2] == 3:
        if list_x[i][1] > O[1]:
            O[1] = list_x[i][1]
    elif list_x[i][2] == 4:
        if list_x[i][1] < MU[1]:
            MU[1] = list_x[i][1]
            
W_ans = MU[0]-O[0]
H_ans = MU[1]-O[1]

if W_ans <0 or H_ans<0:
    print("0")
else:
    ans = W_ans*H_ans
    print(ans)
            



"""
for i in range(N):
    if list_x[i][2] == 1:
        de = list_x[i][0]
        S -= de*H
        W -= de
    elif list_x[i][2] == 2:
        de = W - list_x[i][0]
        S -= de*H
        W -= de
    elif list_x[i][2] == 3:
        de = list_x[i][1]
        S -= de*W
        H -= de
    else:
        de = H - list_x[i][1]
        S -= de*W
        H -= de

print(S)
"""
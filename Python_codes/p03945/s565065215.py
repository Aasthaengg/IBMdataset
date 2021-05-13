# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:09:47 2020

@author: sd18016
"""   

import sys
from itertools import groupby


S = list(input())

ans = len(list(groupby(S)))-1
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
# -*- coding: utf-8 -*-
import numpy as np
# 整数の入力
n, k = map(int, input().split())
numlist = np.arange(1,n+1)
j = 0
if k == 1:
    print(n)
else:
    for i in range(0,n-1):
        a = numlist[i:i+k]
        if a[k-1] == n:
            j += 1
            break
        else:
            j += 1
            pass
    print(j)
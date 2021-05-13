
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(map(int,input().split())))
    return np.array(x)

S = input()

N = len(S)

List = []

for i in range(0,int(N/2)):
    List.append([S[0:i+1],S[i+1:2*i+2]])

del List[-1]

for a in List[::-1]:
    if a[0] == a[1]:
        print(2*len(a[0]))
        exit()


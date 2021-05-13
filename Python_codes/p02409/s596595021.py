# -*- coding: utf-8 -*-
'import sys'
d=[[[0 for i in range(10)]for j in range(3)]for k in range(4)]
n=int(input())
for i in range(n):
    b,f,r,v=[int(j) for j in input().split()]
    d[b-1][f-1][r-1]+=v
for i, b in enumerate(d):
    for f in b:
        for r in f:
            print(" {}".format(r),end="")
        print()
    if i< 3:
        print("#"*20)
# coding: utf-8
import math
h, w = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

i = 0
l = []
flg = True
while i < N:
    if A[i] > 0:
        if flg:
            l.append(str(i+1))
        else:
            l.insert(0,str(i+1))
        A[i] -= 1
    else:
        i += 1
    if len(l) == w:
        print(' '.join(l))
        if flg:
            flg = False
        else:
            flg = True
        l = []
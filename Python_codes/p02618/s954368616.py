# coding: utf-8
# Your code here!
import numpy as np
d= int(input())
 
C = list(map(int,input().split()))
CB = [0 for i in range(len(C))]
 
c = sum(C)
 
total = 0
 
#print(c,C,CB)
L = []
 
for i in range(d):
    L.append(list(map(int,input().split())))
 
#print(L)
 
 
#print(T)
 
def cnt(CB,t):
    for i in range(len(CB)):
        if i != t:
            CB[i] += 1
        else:
            CB[i] = 0
    
    return CB
 
def sumA(C,CB):
    a = 0
    for i in range(len(CB)):
        a += CB[i]*C[i]
    return a
 
def check(L,C,CB):
    a = L[0]+CB[0]*C[0]
    r = 0
    for i in range(len(CB)):
        if a < L[i]+CB[i]*C[i]:
            r = i
    return r
 
for i in range(d):
    ## 最大値で更新
#    ind = np.argmax(L[i])
#    CB = cnt(CB,ind)
#    total += L[i][ind] - sumA(C,CB)
    
    ind = i%26
    CB = cnt(CB,ind)
    total += L[i][ind] - sumA(C,CB)


    print(ind+1)
 
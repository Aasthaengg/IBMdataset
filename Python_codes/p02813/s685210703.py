# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:35:44 2020

@author: liang
"""
#from collections import deque

N = int(input())
P_list = list()

num = list(range(N))
perm = list()

def make_perm():
    #print("start")
    if len(num) == 0:
        P_list.append(perm.copy())
        #print("append")
        return
    for i in range(len(num)):
        t = num.pop(0)
        perm.append(t)
        #print(perm)
        make_perm()
        perm.pop()
        num.append(t)
        
make_perm()
#print(P_list)
P_list.sort()
#print(P_list)

ans = 0
P = [int(x)-1 for x in input().split()]
Q = [int(x)-1 for x in input().split()]
for i in range(len(P_list)):
    if P == P_list[i]:
        a = i
    if Q == P_list[i]:
        b = i
print(abs(a-b))
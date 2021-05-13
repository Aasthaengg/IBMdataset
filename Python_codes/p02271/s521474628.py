# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:28:06 2018
ALDS1_5a_r1  
@author: maezawa
"""
import itertools as itr

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

sum_array = []
for r in range(1,n+1):
    for comb in itr.combinations(a, r):
        sum_array.append(sum(comb))
sum_array.sort()

for i in m:
    left = 0
    right = len(sum_array)
    yesorno = 'no'
    while(left < right):
        #print(left, right)
        mid = (left+right)//2
        if sum_array[mid] == i:
            yesorno = 'yes'
            break
        elif sum_array[mid] > i:
            right = mid
        else:
            left = mid+1
            
    print(yesorno)


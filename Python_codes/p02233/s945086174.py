# -*- coding: utf-8 -*-
"""
Created on Fri May  4 20:13:10 2018
ALDS1_10_A
@author: maezawa
"""

fib_arr = [None for _ in range(45)]
fib_arr[0] = 1
fib_arr[1] = 1

def fib(n):
    if fib_arr[n] != None:
        return fib_arr[n]
    fib_arr[n] = fib(n-1)+fib(n-2)
    return fib_arr[n]
    
n = int(input())
print(fib(n))

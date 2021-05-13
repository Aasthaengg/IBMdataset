# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(100000)

calculated = set([0, 1])
cal_fib = [0 for _ in range(45)]
cal_fib[0:2] = 1, 1

def fib(n):
    if cal_fib[n] == 0:
        cal_fib[n] = fib(n-1) + fib(n-2)
    return cal_fib[n]

n = int(input())
print(fib(n))
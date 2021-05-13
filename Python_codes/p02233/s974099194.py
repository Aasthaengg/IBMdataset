# -*- coding: utf-8 -*-

fib = [1, 1]
for i in range(2, 45):
    fib.append(fib[i-1]+fib[i-2])

n = int(raw_input())
print fib[n]
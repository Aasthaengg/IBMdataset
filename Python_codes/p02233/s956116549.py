#!/usr/bin/python

n = int(input())

def fib(n):
    l = list()
    l.append(1)
    l.append(1)

    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])

    return l[-1]

print(fib(n))
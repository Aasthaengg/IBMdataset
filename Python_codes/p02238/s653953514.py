#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin


def walk(index, tm, L, d, f):
    tm += 1
    d[index] = tm
    for i in L[index]:
        if not d[i-1]:
            tm = walk(i-1, tm, L, d, f)
    tm += 1
    f[index] = tm
    return tm


def main():
    num = int(stdin.readline())

    L = []
    for _ in xrange(num):
        L.append([int(s) for s in stdin.readline().split()[2:]])

    d = [0] * num
    f = [0] * num
    tm = 0
    for i in xrange(num):
        if not d[i]:
            tm = walk(i, tm, L, d, f)

    for i in xrange(num):
        print(i+1, d[i], f[i])


main()
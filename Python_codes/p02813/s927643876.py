#!/usr/bin/python3
#coding: utf-8

from itertools import permutations

N = int(input())
P = input().strip()
Q = input().strip()

nth = 0
np = -1 
nq = -1
for i in permutations(range(N)):
    nth += 1
    s = " ".join([str(x+1) for x in i])
    if s == P:
        np = nth
    if s == Q:
        nq = nth

print(abs(np - nq))

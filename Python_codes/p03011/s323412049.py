# -*- coding: utf-8 -*-
from sys import stdin
input = stdin.readline

A = list(map(int, input().split()))

A.sort()

print(A[0] + A[1])
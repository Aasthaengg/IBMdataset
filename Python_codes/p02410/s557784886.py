#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n, m = map(int, sys.stdin.readline().split())
matrix_a = list()
matrix_b = list()

for i in range(n):
    matrix_a.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    matrix_b.append(int(sys.stdin.readline()))

#print(matrix_a)
#print(matrix_b)

for i in range(n):
    product = 0
    for x in range(m):
        product += matrix_a[i][x]*matrix_b[x]
    print(product)


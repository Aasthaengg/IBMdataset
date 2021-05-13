# -*- coding: utf-8 -*-
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

total = X * (N if N <= K else K)
total += Y * (0 if N <= K else N - K)

print(total)

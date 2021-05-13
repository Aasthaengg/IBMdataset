# -*- coding: <encoding name> -*-

n = int(input())
a = list(map(int, input().split()))

A = sorted(a)
print(A[-1] - A[0])
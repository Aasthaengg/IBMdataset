# -*- coding: utf-8 -*-

INF = 10**9 + 7
n = int(input())
result = 1

for x in range(1, n+1):
    result = result * x % INF

print(result)
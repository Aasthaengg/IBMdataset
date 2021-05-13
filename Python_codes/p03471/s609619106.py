# -*- coding: utf-8 -*-
# 整数の入力
inputs = [int(s) for s in input().split()]
N = inputs[0]
Y = inputs[1]

def check_count():
    for i in range(N+1):
      for j in range(N+1-i):
        k = N - (i+j)
        total = k * 10000 + j * 5000 + i * 1000
        if total == Y:
            return " ".join([str(k), str(j), str(i)])
    return "-1 -1 -1"

print(check_count())

# coding: utf-8

n = int(input())

max_val = -10 ** 10
min_val = int(input())

for i in range(n - 1):
    t = int(input())
    max_val = max(max_val, t - min_val)
    min_val = min(min_val, t)

print(max_val)
# -*- coding: utf-8 -*-

n = int(input())
t_l = list(map(int, input().split()))
m = int(input())
result = []

for i in range(m):
    t_l_i = list(t_l)
    p, x = map(int, input().split())
    t_l_i[p - 1] = x
    result.append(sum(t_l_i))

print(*result, sep='\n')
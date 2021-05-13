# -*- coding: utf-8 -*-
N = int(input())

a_b_ab_list = [ ]
for _ in range(N):
    a, b = map(int, input().split(' '))
    a_b_ab_list.append((a, b, a+b))

a_b_ab_list.sort(key=lambda x: x[2], reverse=True)

t, a = 0, 0
for i in range(0, N, 2):
    t += a_b_ab_list[i][0]

for i in range(1, N, 2):
    a += a_b_ab_list[i][1]

print(t - a)
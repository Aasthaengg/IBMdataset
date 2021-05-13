# -*- coding: utf-8 -*-

n = int(input())
s = list(input())

answer_sum = [0] * n
e_sum = [0] * (n+1)
w_sum = [0] * (n+1)

for i in range(n):
    w_sum[i+1] = (s[i] == 'W') + w_sum[i]
    e_sum[i+1] = (s[i] == 'E') + e_sum[i]

for i in range(n):
    answer_sum[i] = w_sum[i] + (e_sum[n] - e_sum[i+1])

print(min(answer_sum))
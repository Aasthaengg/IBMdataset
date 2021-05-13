# -*- coding: utf-8 -*-

[N, A, B] = [int(i) for i in input().split()]

plan_1 = A * N

plan_2 = B

print(min(plan_1, plan_2))
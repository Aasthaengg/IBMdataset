# -*- coding: utf-8 -*-

def get_diff(T, A, x):
    temp = T - x * 0.006
    return abs(temp - A)


N = int(input())
T,A = map(int, input().split())
H_list = list(map(int, input().split()))

for i, h in enumerate(H_list):
    if i==0:
        diff_min = get_diff(T, A, h)
        diff_min_idx = i + 1
    else:
        diff = get_diff(T, A, h)
        if diff_min > diff:
            diff_min = diff
            diff_min_idx = i + 1 

print(diff_min_idx)

# -*- coding: utf-8 -*-

def get_digits_sum(val_str):
    digits_sum = 0
    for i in range(len(val_str)):
        digits_sum += int(val_str[i])

    return digits_sum

N = int(input())

if N==2:
    sum_min = 2

for i in range(2, N, 1):
    A = i
    B = N - i
    a_sum = get_digits_sum(str(A))
    b_sum = get_digits_sum(str(B))
    if i==2:
        sum_min = a_sum + b_sum
    elif sum_min > a_sum + b_sum:
        sum_min = a_sum + b_sum
        
print(sum_min)
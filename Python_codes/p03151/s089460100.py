# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

if sum(A) < sum(B):
    print(-1)
    exit()

positives = []
sum_negative = 0
num_negative = 0
for a, b in zip(A, B):
    if a > b:
        positives.append(a - b)

    elif a < b:
        sum_negative += b - a
        num_negative += 1


positives.sort(reverse=True)

num_positives = len(positives)
while positives and sum_negative > 0:
    p = positives.pop(0)
    sum_negative -= p

print(num_positives - len(positives) + num_negative)
import sys

n = int(input())
a = list(map(int, input().split()))

min_a = 0
sum_a = 0
for i in range(n):
    sum_a += a[i]
    if i % 2 == 0:
        if sum_a <= 0:
            min_a += abs(sum_a) + 1
            sum_a += abs(sum_a) + 1
    else:
        if sum_a >= 0:
            min_a += abs(sum_a) + 1
            sum_a -= abs(sum_a) + 1

min_b = 0
sum_b = 0
for i in range(n):
    sum_b += a[i]
    if i % 2 == 0:
        if sum_b >= 0:
            min_b += abs(sum_b) + 1
            sum_b -= abs(sum_b) + 1
    else:
        if sum_b <= 0:
            min_b += abs(sum_b) + 1
            sum_b += abs(sum_b) + 1

print(min(min_a, min_b))

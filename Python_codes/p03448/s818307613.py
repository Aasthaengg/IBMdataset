# -*- coding: utf-8 -*-
# 整数の入力

A = int(input())
B = int(input())
C = int(input())
X = int(input())

i = 0
j = 0
k = 0
cnt = 0
sum = 0
while i <= A:
    j = 0
    if i>50:
        break
    while j <= B:
        k = 0
        if j>50:
            break
        while k <= C:
            if k>50:
                break
            else:
                sum = 500*i + 100*j + 50*k
                if X == sum:
                    cnt += 1
                k += 1
                sum = 0
        j += 1
    i += 1

print(cnt)
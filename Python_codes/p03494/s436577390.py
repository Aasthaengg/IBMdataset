# coding: utf-8
import math
N = input()
A = list(map(int, input().split()))

count = 0
while True:
    for i, a in enumerate(A):
        if a % 2 == 0:
            A[i] = a / 2
        else:
            print(count)
            exit()
    count = count + 1


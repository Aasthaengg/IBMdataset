# coding: utf-8

N, A, B = map(int, input().split())

largest = min(A, B)
minimum = max(0, A + B - N)

print(largest, minimum)

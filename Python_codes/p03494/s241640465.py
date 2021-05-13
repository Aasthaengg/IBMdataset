# coding: utf-8

N = int(input())
A = list(map(int, input().split()))

count = 0
imp = 0

while True:
    for i in range(0, N):
        if int(A[i]) % 2 == 1:
            imp = 1
            break

    if imp == 1:
        break

    for i in range(0, N):
        A[i] = int(A[i] / 2)
    count += 1

print(count)
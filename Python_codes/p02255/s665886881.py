# coding: utf-8
n = int(input())
data = [int(i) for i in input().split()]

for i in range(n):
    v = data[i]
    j = i - 1
    while j >= 0 and data[j] > v:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = v
    print(*data)
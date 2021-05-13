# coding: utf-8
A, B = map(int, input().split())
lst = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            lst.append(i * 10000 + j * 1000 + k * 100 + j * 10 + i)

ans = [0 for i in lst if A <= i <= B]
print(len(ans))
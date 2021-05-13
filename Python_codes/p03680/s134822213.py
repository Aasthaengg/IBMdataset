# -*- coding: utf-8 -*-

n = int(input())

a = []
for i in range(n):
    a.append(int(input()))

note = [0] * n
i = 0
step = 0
ret = -1
while True:
    if note[i] == 1:
        break
    if i == 1:
        ret = step
        break
    note[i] = 1
    i = a[i] - 1
    step += 1


print(ret)
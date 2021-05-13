# coding: utf-8

N = int(input())

count = 0
for i in range(1, N+1, 2):
    i_yakusu = 0
    for j in range(1, i+1):
        if i % j == 0:
            i_yakusu += 1
    if i_yakusu == 8:
        count += 1

print(count)
# -*- coding: utf-8 -*-

def counter(num):
    cnt = 0
    while True:
        if num % 2 == 0:
            num = int(num/2)
            cnt += 1
        else:
            break

    return cnt



N = int(input())

max_cnt = 0
max_num = num = N
for num in range(N,0,-1):
    cnt = counter(num)
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = num   

print(max_num)
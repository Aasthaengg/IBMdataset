#!/usr/bin/python
# -*- coding:utf-8 -*-

load_num, track_num = list(map(int, input().split(" ")))

loads = list()
for _ in range(load_num):
    loads.append(int(input()))

P = 10000 * 100000

def isMeet(p):
    i = 0

    for _ in range(track_num): # ??????????????°??°???????????????
        sum = 0 # ???????????????????????????
        while (sum + loads[i] <= p):
            sum += loads[i]
            i += 1
            if i == load_num:
                return True
    return False


def binary_search(P):
    left = 0 
    right = P
    while right - left > 0:
        mid = int((left+right)/2)
        if isMeet(mid):
            right = mid
        else:
            left = mid + 1
    return right

print(binary_search(P))
# -*- coding: utf-8 -*-

N,M = list(map(int, input().rstrip().split()))
ab_list = [list(map(int, input().rstrip().split())) for i in range(M)]
#-----

ab_list.sort(key= lambda x: x[1])

prev_tail = -float("inf")
cnt = 0

for left,right in ab_list:
    if prev_tail <= left:
        cnt += 1
        prev_tail = right

print(cnt)

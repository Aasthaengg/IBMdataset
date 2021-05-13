#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

num = input()
nums = [int(num[0]), int(num[1]), int(num[2]), int(num[3])]

sum_ = sum(nums)

for bit in range(1 << 3):
    tmp = sum_
    ops = ['+', '+', '+']
    for j in range(3):
        if bit & (1 << j):
            tmp -= 2 * nums[j+1]
            ops[j] = '-'
    if tmp == 7:
        res = str(nums[0]) + ops[0] + str(nums[1]) + ops[1] + str(nums[2]) + ops[2] + str(nums[3]) + '=7'
        print(res)
        break

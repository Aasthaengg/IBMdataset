# -*- coding: utf-8 -*-

input_nums = input().split()
multiplied_num = int(input_nums[0])*int(input_nums[1])

if multiplied_num%2==0:
    print("Even")
else:
    print("Odd")

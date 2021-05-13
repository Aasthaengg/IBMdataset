import sys
# -*- coding: utf-8 -*-

#calc("",1234) = calc("1",234) + calc("1+"",234)
#calc("1",234) = calc("12",34) + calc("12+",34)
#calc("12+",34) = calc("12+3",4) + calc("12+3+",4)
#calc("12+3",4) = calc("12+34")
def calc(express,i):
    if i == len(nums):
        return sum(list(map(int,express.split("+"))))
    return calc(express + nums[i],i+1) + calc(express + "+"+ nums[i] ,i+1) 

nums = list(input())
print(calc(nums[0],1))

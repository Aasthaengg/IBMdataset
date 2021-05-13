# coding:utf-8
import math
array = map(float,raw_input().split())
x1 = array[0]
y1 = array[1]
x2 = array[2]
y2 = array[3]
answer = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
print answer


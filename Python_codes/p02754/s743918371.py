# coding: utf-8
import math

count = 0
num, blue_num, red_num = map(int, input().split())
all_ball = blue_num + red_num
count = num // all_ball
rest = num % all_ball
print(count * blue_num + min(rest, blue_num))

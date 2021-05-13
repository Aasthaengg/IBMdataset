#coding:utf-8
#1_10_A 2015.4.10
import math

position = list(map(float,input().split()))
distance = math.sqrt((position[2] - position[0]) ** 2 + (position[3] - position[1]) ** 2)
print('{:.5f}'.format(distance))
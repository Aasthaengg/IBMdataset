#coding: UTF-8
import math

p = list(map(float, input().split()))
# dis = math.sqrt(pow((abs(p[2]) - abs(p[0])), 2) + pow((abs(p[3]) - abs(p[1])), 2))
dis = math.sqrt(pow((p[2] - p[0]), 2) + pow((p[3]) - (p[1]), 2))

print(round(dis, 8))

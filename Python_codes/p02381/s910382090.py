#coding:utf-8
#1_10_C 2015.4.14
import math

while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int,input().split()))
    ave = sum(scores)/n
    sd = math.sqrt(sum([(s - ave)**2 for s in scores])/n)
    print('{:.10f}'.format(sd))
#coding:utf-8
import math

N,X,T = map(int,input().split())

print("{}".format(math.ceil(N / X) * T))
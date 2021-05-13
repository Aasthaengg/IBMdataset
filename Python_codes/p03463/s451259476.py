# -*- coding: utf-8 -*-
#AGC020A
import sys
#import collections

#n= int(input())
tmp = input().split()
n,a,b = list(map(lambda a: int(a), tmp))

if((b-a)%2==0):
	print("Alice")
else:
	print("Borys")



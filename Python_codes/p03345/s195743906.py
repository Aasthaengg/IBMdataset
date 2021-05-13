# -*- coding: utf-8 -*-
#AGC024A
import sys
#import collections

#n= int(input())
#s= input()
tmp = input().split()
a,b,c,k = list(map(lambda a: int(a), tmp))

if(k%2==1):
	print(b-a)
else:
	print(a-b)

#import sys
#import math
import numpy as np
'''a,b= map(int,input().split())'''
#a, b, c = [list(map(int, input().split())) for _ in range(3)]
#li0= [int(x) for x in input().split()]
#n,l= map(int, input().split())
#x = [list(map(int, input().split())) for _ in range(n)] 
a,b,c=map(int,input().split())
count=c
for i in range(10):
  count=a*count-b
  print(count)
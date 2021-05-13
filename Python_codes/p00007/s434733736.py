'''
Created on Mar 11, 2013

@author: wukc
'''
import math
n=int(raw_input())

p=100000
for i in range(n): p=int(math.ceil(p*1.05/1000)*1000)
print p
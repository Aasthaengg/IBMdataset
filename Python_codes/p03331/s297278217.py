
import sys  
import numpy as np

input = sys.stdin.readline

N = input()
sum_ = 0

for i in list(N)[:-1]:
    
    sum_+=int(i)

if sum_ != 1:
    print(sum_)
else :
    print(10)

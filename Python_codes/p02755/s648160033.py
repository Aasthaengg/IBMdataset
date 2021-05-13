# coding: utf-8
# Your code here!
import numpy as np
import sys
A,B=map(int,input().split())


for i in range(1,10000):
    if int(i*0.08)==A and int(i*0.10)==B:
        print(i)
        sys.exit()
print(-1)
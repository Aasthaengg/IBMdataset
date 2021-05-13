#
import sys
import math
import numpy as np
import itertools

# いくつか入力
n,h,w = (int(i) for i in input().split())  

# n行複数列の数をリストに
ab = [[int(i) for i in input().split()] for i in range(n)] 

answer = 0

for i in range(n):
    if(h <= ab[i][0] and w <= ab[i][1]):
        answer += 1

print(answer)



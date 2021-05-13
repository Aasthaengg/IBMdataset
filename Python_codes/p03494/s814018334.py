import sys
import copy
import math
import itertools
N = int(input())
A = [int(c) for c in input().split()]
cnt = 0

while sum(list(map(lambda x:x%2,A)))==0:
    A=list(map(lambda x:int(x/2),A))
    cnt+=1

print(cnt)
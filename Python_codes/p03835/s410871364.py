import math
import sys
from collections import deque
a,b=map(int,input().split())
count=0
for i in range(a+1):
  for j in range(a+1):
    if 0<=b-i-j<=a:
      count+=1
print(count)
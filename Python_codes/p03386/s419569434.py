import math
import re
import copy
import sys

a,b,k = map(int,input().split())

for i in range(a,min(a+k,b+1)):
    print(i)

for j in range(max(b-k+1,i+1),b+1,1):
    print(j)
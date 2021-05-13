import sys
import math
import itertools
n = int(input())
if(n%2==0):
    print((n + 1) * (n // 2) - n)
else:
    print((n + 1) * ((n-1) // 2) +(n+1)//2- n)
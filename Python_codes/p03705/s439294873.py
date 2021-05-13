import sys
input = sys.stdin.readline
from collections import *

N, A, B = map(int, input().split())

if A>B:
    print(0)
    exit()

if N==1 and A!=B:
    print(0)
    exit()
    
low = A+B+(N-2)*A
high = A+B+(N-2)*B
print(high-low+1)
import sys
import copy
import math
import itertools

a = [int(c) for c in input().split()]
N=a[0]
A=a[1]
B=a[2]

if N % (A+B) >= A:
    cnt=A
else:
    cnt=N % (A+B)

cnt += int(N/(A+B))*A
print(cnt)
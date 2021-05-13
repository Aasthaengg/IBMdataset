"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd
import sys
#input = sys.stdin.readline

import copy"""

K=int(input())
N=50
A=[0 for i in range(N)]


if K<=49:
	A[0]=49+K*50
else:
	A=[i for i in range(1,N+1)]
	K-=50
	for i in range(50):
		A[i]+=K//50
	for i in range(K%50):
		A[49-i]+=1


print(50)
print(" ".join([str(i) for i in A]))
"""
count=0
while 1:

	idx=[i for i in range(50) if A[i]==max(A) and A[i]>=50]
	if not idx:
		break
	i=idx[0]
	A[i]-=50
	for m in range(50):
		if i!=m:
			A[m]+=1
	count+=1
print(A)
print(count)
"""

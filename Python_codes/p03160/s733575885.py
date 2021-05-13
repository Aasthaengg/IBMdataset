import math
import os
import random
import re
import sys
def dpfindpath(a):
	dpath=[int(0) for _ in range(len(a))]
	dpath[0]=0
	dpath[1]=abs(a[1]-a[0])
	for i in range(2,len(a)):
		dpath[i]=min(abs(a[i]-a[i-1])+dpath[i-1],abs(a[i]-a[i-2])+dpath[i-2])
	return dpath[len(a)-1]
n=int(input())
a=input().split()
for i in range(n):
  a[i]=int(a[i])
print (dpfindpath(a))

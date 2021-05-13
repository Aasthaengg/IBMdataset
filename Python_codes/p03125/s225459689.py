import sys
import math
import itertools

a,b=list(map(int,input().split()))
for i in range(1,b+1,1):
	if b%a==0:
		print(a+b)
		sys.exit()
print(b-a)
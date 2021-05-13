import sys
import math
import itertools

a,b,c=list(map(int,input().split()))
count=math.floor(b/a)
if (count>=c):
	print(c)
	sys.exit()
print(count)
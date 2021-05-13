h=int(input())
w=int(input())
n=int(input())
if h<w:
	w,h=h,w
from math import ceil
print(ceil(n/h))
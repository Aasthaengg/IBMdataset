from math import *

def trycut(val):
	if val == 0 : return float('inf')
	ret = 0
	for i in range(n):
		ret += (a[i]+val-1)//val -1
	return ret 

n,k=map(int,input().split())
a = [int(i) for i in input().split()]

low = 0
high = max(a)
ans  =-1

while low <= high:
	mid = (low + high)//2
	cut = trycut(mid)
	if cut <= k:
		high = mid-1
		ans = mid
	else:
		low =  mid+1
print(ans)



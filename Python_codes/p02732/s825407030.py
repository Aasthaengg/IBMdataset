n=int(input())
a=list(map(int,input().split()))

import collections
C = collections.Counter(a)

#logging.debug(C)

sum=0
for v in list(C.values()):
	sum+=v*(v-1)//2
 
for k in range(n):
	x = C[a[k]]
	print(sum-(x*(x-1)//2)+((x-1)*(x-2)//2))
import math
l,r,d = (int(i) for i in input().split())
z = int(math.floor(r/d)-math.floor(l/d))
if l%d == 0:
	print(z+1)
else:
	print(z)

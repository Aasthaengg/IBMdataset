import math
n=int(input())
r=100000
for i in range(n):
	r=math.ceil(r*1.05/1000)*1000
print(r)
import math
a,b = map(int,input().split())
c = 0
for i in range(a,b+1):
	if i%10 == math.floor(i//10000)%10 and math.floor(i//1000)%10 == math.floor(i//10)%10:
		c += 1
print(c)
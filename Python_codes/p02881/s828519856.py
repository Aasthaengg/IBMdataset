import math
n=int(input())
a=0
b=10**12
for i in range(1, 1+int(math.sqrt(n))):
	if n%i==0:
		a=(i-1)+(n//i)-1
	if a<b:
		b=a
print(b)
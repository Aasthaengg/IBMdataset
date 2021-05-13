import math

n = int(input())
d = 100000

for i in range(n):
	d *= 1.05
	d = math.ceil((d/1000))*1000
print(d)
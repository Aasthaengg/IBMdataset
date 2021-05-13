from math import ceil
n=int(input())
d=int(1e5)
for x in range(n):
	d=(1.05*d)
	d=int(int(ceil(d/1e3))*1e3)
print(d)
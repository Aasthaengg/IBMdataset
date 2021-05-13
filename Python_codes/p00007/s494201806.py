import math as k
n=input()
m=105
for i in range(n-1):
	m=k.ceil(m*1.05)
print int(m*1000)
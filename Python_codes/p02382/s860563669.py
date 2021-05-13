import math
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

def suan(p):
	d = 0
	for i in range(n):
		d += (math.fabs(x[i] - y[i]))**p
	print('%.6f'%(d**(1/p)))

suan(1)
suan(2)
suan(3)
print(max(math.fabs(x[i] - y[i])for i in range(n)))

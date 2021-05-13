n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

dsum1 = 0
dsum2 = 0
dsum3 = 0
dmax = 0
for i in range(len(x)):
	d = abs(x[i]-y[i])
	dsum1 += d
	dmax = max(dmax, d)
	dsum2 += d**2
	dsum3 += d**3
print('{0:.6f}'.format(dsum1))
print('{0:.6f}'.format(dsum2**(1/2)))
print('{0:.6f}'.format(dsum3**(1/3)))
print('{0:.6f}'.format(dmax))

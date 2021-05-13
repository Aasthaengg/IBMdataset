n = input()
x = map(int, raw_input().split())
y = map(int, raw_input().split())

sum1 = 0.00
for i in range(n):
	sum1 += abs(x[i]-y[i])
print '%.6f'%sum1

sum2 = 0.00
for i in range(n):
	sum2 += pow(abs(x[i]-y[i]), 2)
print '%.6f'%pow(sum2, 0.5)

sum3 = 0.00
for i in range(n):
	sum3 += pow(abs(x[i]-y[i]), 3)
print '%.6f'%pow(sum3, 1.00/3)

sum4 = 0.00
for i in range(n):
	sum4 = max(sum4, abs(x[i]-y[i]))
print '%.6f'%(sum4)
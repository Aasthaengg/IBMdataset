n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
p1,p2,p3 = 0,0,0
pin = []
for i in range(n):
	p1 += abs(x[i] - y[i])
	p2 += abs(x[i] - y[i])**2
	p3 += abs(x[i] - y[i])**3
	pin.append(abs(x[i] - y[i]))
p2 = p2**(1/2)
p3 = p3**(1/3)
pinf = max(pin)
print(p1)
print(p2)
print(p3)
print(pinf)

import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0

for i in range(n):
	a = math.fabs(x[i] - y[i])
	ans1 += a
	ans2 += a**2
	ans3 += a**3
	ans4 = max(ans4, a) 

print(ans1)
print(ans2**(1./2.))
print(ans3**(1./3.))
print(ans4)

from math import pow
d,n = map(int,input().split())
ans = pow(100,d)*n
if n==100:
	ans += pow(100,d)
print (int(ans))


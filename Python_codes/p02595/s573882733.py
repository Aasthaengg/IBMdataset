import math
n,distance = map(int, input().split())
res = 0
for i in range(n):
	a, b = map(int ,input().split())
	if abs(a) > distance or abs(b)> distance:continue
	elif math.sqrt(a*a+b*b)>distance:continue
	res += 1
print(res)
import math
n=int(input())
ans=100000
for i in range(n):
	ans*=1.05
	ans=int(math.ceil(ans/1000)*1000)
print(ans)


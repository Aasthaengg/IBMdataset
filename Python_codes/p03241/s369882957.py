import math
n, m = map(int, input().split())

ans = 1
for i in range(1,math.ceil(math.sqrt(m))):
	if m%i == 0:
		if m >= n*i:
			ans = max(ans, i)
		j = m//i
		if m >= n*j:
			ans = max(ans,j)

print (ans)
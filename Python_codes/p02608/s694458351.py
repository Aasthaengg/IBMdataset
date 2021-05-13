n = int(input())

ans = [0]*(n+1)

for x in range(1,100):
	for y in range(1,100):
		for z in range(1,100):
			if pow(x,2) + pow(y,2) + pow(z,2) + x*y + y*z + z*x <= n:
				ans[pow(x,2) + pow(y,2) + pow(z,2) + x*y + y*z + z*x] += 1			
for i in range(1,n+1):
	print(ans[i])
# D - Sum of Divisors
N = int(input())
ans = 0

for i in range(1, N + 1):
	j = 1
	
	while True:
		if i * j <= N:
			#print(i * j)
			
			ans += i * j
			j += 1
		else:
			break

print(ans)
	

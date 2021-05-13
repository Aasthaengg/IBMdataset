N = int(input())
K = int(input())

sum = 1
for i in range(1, N+1):
	if sum*2 >= sum+K:
		sum += K
	else:
		sum = 2*sum

print(sum)
a, b = list(map(int, input().split()))

res = 1
n_a = 0
while res < b:
	res += a - 1
	n_a += 1
	
print(n_a)
n, k = map(int, input().split())
result = 0
if k % 2 == 0:
	counter = (n - k // 2) // k
	result += (counter + 1) ** 3
	counter = n // k
	result += counter ** 3
else:
	counter = n // k
	result = counter ** 3

print(result)
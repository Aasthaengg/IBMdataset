n = int(input())
for i in range(n - 1, 1, -1):
	n *= i
	n %= 10**9 + 7
print(n)
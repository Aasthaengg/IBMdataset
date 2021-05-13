n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))

ac = 0

for _ in range(n):
	res = c
	a = list(map(int, input().split()))
	for x, y in zip(a, b):
		res += x * y
	
	if res > 0:
		ac += 1

print(ac)
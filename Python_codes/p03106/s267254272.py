a, b, k = map(int, input().split())
cnt = 0
i = 0
lst = []
while i <= max(a,b):
	i += 1
	if a % i == 0 and b % i == 0:
		lst.append(i)
print(lst[-k])


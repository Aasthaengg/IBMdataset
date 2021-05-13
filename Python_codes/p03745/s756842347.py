n = int(input())
a = list(map(int, input().split()))

res = 0
i = 0
while i < n:
	# sama
	while (i + 1 < n and a[i] == a[i + 1]):
		i += 1

	if i + 1 < n and a[i] < a[i + 1]:
		while i + 1 < n and a[i] <= a[i + 1]:
			i += 1

	elif i + 1 < n and a[i] > a[i + 1]:
		while i + 1 < n and a[i] >= a[i + 1]:
			i += 1
	res += 1
	i += 1

print(res)

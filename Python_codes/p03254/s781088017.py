n, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
count = 0
for i in range(n - 1):
	if A[i] <= x:
		x -= A[i]
		count += 1
	else:
		print(count)
		exit()
print(count if x != A[n - 1] else count + 1)
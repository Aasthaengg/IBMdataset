n = int(input())
maxv = 0
for i in range(1, n + 1):
	if i**2 > n:
		break
	maxv = i**2
print(maxv)
n = int(input())
a = [int(input()) for i in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
	if i == 0 and a[i] != 0:
		print(-1)
		exit()
	else:
		if a[i - 1] + 1 < a[i]:
			print(-1)
			exit()
		elif a[i - 1] + 1 == a[i]:
			ans += 1
		else:
			ans += a[i]
print(ans)
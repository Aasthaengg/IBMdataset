n = int(input())
a = [int(input()) for _ in range(n)]
 
if a[0] != 0:
	print(-1)
else:
	ans = 0
	muri = 0
 
	for i in range(1, n):
		if a[i] > a[i-1] + 1:
			muri = 1
		elif a[i] < a[i-1] + 1:
			ans += a[i-1]
			if i == n - 1:
				ans += a[i]
		elif i == n - 1:
			ans += a[i]
 
	if muri:
		print(-1)
	else:
		print(ans)
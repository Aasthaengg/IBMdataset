n, k = map(int,input().split())
ans = 1
if n == 1:
	print(k)
else:
	ans = k*((k-1)**(n-1))
	print(ans)

n,k,s = map(int,input().split())
if k == 0:
	if s != 10**9:
		print(" ".join([str(10**9) for _ in range(n)]))
	else:
		print(" ".join([str(1) for _ in range(n)]))
elif s != 10**9:
	ans = [10**9 for _ in range(n)]
	for i in range(k):
		ans[i] = s
	print(" ".join([str(ans[i]) for i in range(n)]))
else:
	ans = [1 for _ in range(n)]
	for i in range(k):
		ans[i] = s
	print(" ".join([str(ans[i]) for i in range(n)]))
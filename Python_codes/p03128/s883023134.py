def larger(x, y):
	if len(x) > len(y):
		return x
	elif len(x) < len(y):
		return y
	else:
		if x > y:
			return x
		return y

matchuse = [5000000000000000, 2, 5, 5, 4, 5, 6, 3, 7, 6]
N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[]]
for i in range(0, 10):
	dp[0].append('')
made = []
for i in range(0, N+1):
	lst = []
	for j in range(0, M):
		lst.append(False)
	made.append(lst)
made[0][0] = True
for i in range(1, N+1):
	lst = []
	for j in range(0, M):
		next = ''
		if i - matchuse[A[j]] >= 0:
			index = i - matchuse[A[j]]
			for k in range(0, M):
				if made[index][k]:
					next = larger(next, dp[index][k]+str(A[j]))
		lst.append(next)
		if next != '':
			made[i][j] = True
	dp.append(lst)
ans = ''
for i in range(0, M):
	ans = larger(ans, dp[N][i])
print(ans)
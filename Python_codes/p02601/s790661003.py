A, B, C = list(map(int, input().split()))
K = int(input())

def dfs(k, a, b, c):
	if k == 0:
		if b > A and c > b:
			return True
		else:
			return False

	if dfs(k - 1, a * 2, b, c):
		return True

	if dfs(k - 1, a, b * 2, c):
		return True

	if dfs(k - 1, a, b, c * 2):
		return True

	return False

r = dfs(K, A, B, C)
if r:
	print('Yes')
else:
	print('No')
n, k = map(int, input().split())
L = [int(input()) for i in range(n)]

def check(P):
	global n, k, L
	i = 0
	for j in range(k):
		s = 0
		while s + L[i] <= P:
			s += L[i]
			i += 1
			if i == n:
				return n
	return i

def solve():
	left = 0
	right = 100000 * 10000

	while right - left > 1:
		mid = (left + right) // 2
		v = check(mid)
		if v >= n:
			right = mid
		else:
			left = mid

	return right

print(solve())


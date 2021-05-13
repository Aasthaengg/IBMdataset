n, k = map(int, input().split())
A = list(map(int, input().split()))

# 最大公約数
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

MAX = max(A)
GCD = 0
for i in range(n):
	GCD = gcd(GCD, A[i])

if k % GCD == 0 and k <= MAX:
	print('POSSIBLE')
else:
	print('IMPOSSIBLE')
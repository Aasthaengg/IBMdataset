import fractions
n = int(input())
t = [int(input()) for _ in range(n)]
def lcm(a, b):
	return a*b//fractions.gcd(a, b)
if n == 1:
	print(t[0])
else:
	ans = lcm(t[0], t[1])
	for i in range(2, n):
		ans = lcm(ans, t[i])
	print(ans)
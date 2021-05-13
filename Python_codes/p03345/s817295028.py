a, b, c, k = map(int, input().split())
ans = 0
if (k % 2):
	ans = b - a
else:
	ans = a - b
print(ans if ans <= 10**18 else "Unfair")
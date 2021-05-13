n, x = list(map(int, input().split()))
children = list(map(int, input().split()))
children.sort()

ans = 0
for i in range(n):
	x = x - children[i]
	if i < n - 1:
		if x >= 0:
			ans += 1
	else:
		if x == 0:
			ans += 1

print(ans)
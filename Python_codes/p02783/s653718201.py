h, a = map(int, input().split())
ans, r = divmod(h, a)
if r:
	ans += 1
print(ans)
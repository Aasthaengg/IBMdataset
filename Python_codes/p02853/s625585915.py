X, Y = map(int, input().split())
ans = 0
for i in [X, Y]:
	if i < 4:
		ans += (4 - i) * 10**5
if ans == 6 * 10**5:
	ans = 10 * 10**5
print(ans)
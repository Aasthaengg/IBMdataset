X, Y = map(int, input().split())
ans = 0
ans += max(0, 4 - X)
ans += max(0, 4 - Y)
if(X == 1 and Y == 1):
	ans += 4
ans *= 100000
print(ans)
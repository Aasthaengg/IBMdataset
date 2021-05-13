X, Y = map(int, input().split())
ans = 1
while(1):
	if Y < X*(2**(ans-1)):
		ans -= 1
		break
	ans += 1
print(ans)
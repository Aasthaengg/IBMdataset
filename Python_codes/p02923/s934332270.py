N = int(input())
H = list(map(int, input().split()))
ans = 0
now = 0
for i in range(1, N):
	if H[i - 1] >= H[i]:
		now += 1
		ans = max(ans, now)
	else:
		now = 0
print(ans)

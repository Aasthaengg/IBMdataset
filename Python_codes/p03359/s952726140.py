# A - Day of Takahashi
a, b = map(int ,input().split())
ans = 0

for i in range(1, 13):
	if i < a:
		ans += 1
	elif i == a and i <= b:
		ans += 1

print(ans)
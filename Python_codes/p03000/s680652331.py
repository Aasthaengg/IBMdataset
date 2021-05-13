n, x = map(int, input().split())
list = list(map(int, input().split()))
count, now = 1, 0
for i in range(n):
	now += list[i]
	if now > x:
		break
	count += 1
print(count)

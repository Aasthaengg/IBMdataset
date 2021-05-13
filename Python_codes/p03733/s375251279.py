n, j = map(int, input().split())
t = [int(i) for i in input().split()]

ans = 0

for i in range(1, len(t)):
	if t[i] - t[i-1] < j:
		ans += (t[i] - t[i-1])
	else:
		ans += j

print(ans + j)

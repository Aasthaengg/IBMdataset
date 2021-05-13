# A - Thumbnail
N = int(input())
a = list(map(int, input().split()))

avg = sum(a) / N
min = avg

for i in range(N):
	if abs(a[i] - avg) < min:
		min = abs(a[i] - avg)
		ans = i

print(ans)
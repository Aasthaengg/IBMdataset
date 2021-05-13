N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

count = 0
for a, b in AB:
	if H <= a and W <= b:
		count += 1
print(count)

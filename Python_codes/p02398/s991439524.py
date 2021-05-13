a, b, c = map(int, raw_input().split())
counter = 0
for i in range(b-a+1):
	if c%a == 0:
		counter += 1
	a += 1
print counter	
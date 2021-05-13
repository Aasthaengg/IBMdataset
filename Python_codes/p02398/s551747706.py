l = map(int, raw_input().split())

count = 0

for i in range(l[0],l[1]+1):
	if l[2] % i == 0:
		count += 1

print count
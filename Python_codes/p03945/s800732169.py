line = list(input())
temp = line[0]
cnt = 0
for c in line[1:]:
	if temp != c:
		cnt += 1
		temp = c

print(cnt)
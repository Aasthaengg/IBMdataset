s = input().rstrip()
p = input().rstrip()

for i in range(len(s)):
	cmp = ''
	for j in range(len(p)):
		cmp += s[(i+j) % len(s)]
	if p == cmp:
		print('Yes')
		exit(0)
print('No')

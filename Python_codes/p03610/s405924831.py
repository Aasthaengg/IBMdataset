s = input()
i = 0
r = ''
for t in s:
	if i % 2 == 0:
		r += t
	i += 1
print(r)
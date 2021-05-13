S = input()
d = {}
for s in S:
	if s in d:
		d[s] += 1
	else:
		d[s] = 1
if len(d) == 2 and max(d.values()) == 2:
	print('Yes')
else:
	print('No')

s = int(raw_input())
seen= set()
i = 0
while(s not in seen):
	seen.add(s)
	i +=1
	if s % 2: s = 3 * s + 1
	else: s /= 2
print i+1
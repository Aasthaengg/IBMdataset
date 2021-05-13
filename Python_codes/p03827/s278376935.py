m,c,n = 0,0, raw_input()
for l in raw_input():
	c += 1 if l == 'I' else -1
	m = max(c,m)
print m


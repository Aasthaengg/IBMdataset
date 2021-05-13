s = raw_input()
p = raw_input()
i = 0
while i<len(s):
	k = 0
	while k < len(p):
		if s[(i+k)%len(s)] == p[k]:
			k += 1
		else:
			break
	if k >= len(p):
		print 'Yes'
		break
	i += 1
if k < len(p):
	print 'No'
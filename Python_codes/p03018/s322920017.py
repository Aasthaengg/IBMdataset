s = raw_input()
count = 0
num = 0
i = 0
length = len(s)
while i < length:
	if s[i] == 'A':
		num += 1
		i += 1
	elif i+1 < len(s) and s[i] == 'B' and s[i+1] == 'C':
		count += num
		i += 2
	else:
		num = 0
		i += 1
print count

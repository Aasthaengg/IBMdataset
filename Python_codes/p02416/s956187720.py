s = raw_input()
while s != "0":
	sum = int(s[0])
	for i in range(1,len(s)):
		sum += int(s[i])
	print sum
	s = raw_input()
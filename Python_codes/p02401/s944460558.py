while True:
	s = raw_input().rstrip().split(" ")
	a = int(s[0])
	b = int(s[2])
	if s[1]=="?":break
	if s[1]=="+":print a+b
	if s[1]=="-":print a-b
	if s[1]=="*":print a*b
	if s[1]=="/":print a//b
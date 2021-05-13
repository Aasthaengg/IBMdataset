s = str(input())
if(len(s)==2):
	print(s)
else:
	s1=""
	for i in range(0,len(s)):
		s1=s1+s[len(s)-1-i:len(s)-i]
	print(s1)
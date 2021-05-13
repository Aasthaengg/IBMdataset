s=input()
l1=''
l2=''
if '+' in s:
	s=s.split('+')
	print(int(s[0])+int(s[1]))
else:
	s=s.split('-')
	print(int(s[0])-int(s[1]))
	

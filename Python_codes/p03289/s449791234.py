s=list(input())
s1=s[2:-1]
f=True
if s[0]!='A':
	f=False
elif 'C' not in s1:
	f=False
else:
	s.remove('A')
	s.remove('C')
	if str(s).islower():
		pass
	else:
		f=False
if f:
	print('AC')
else:
	print('WA')
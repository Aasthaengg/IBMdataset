w = input().lower()
s = input().split()
c=0
while (s[0] != 'END_OF_TEXT'):
	for i in range(len(s)):
		if(w==s[i].lower()):
			c+=1
	s = input().split()
print(c)

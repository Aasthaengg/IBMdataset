s = input()

flag = 0

if s.count('C')*s.count('F')==0:
	print('No')
	exit()
	
for i in range(len(s)):
	if s[i]=='C':
		flag = 1
	if flag == 1 and s[i]=='F':
		print('Yes')
		exit()

print('No')

s=input()
l=list(s)
#print(l)
if(l[-1]=='s'):
	l.append('e')
	l.append('s')
else:
	l.append('s')
#print(l)
str1=""

for i in l:
	str1+=i
print(str1)

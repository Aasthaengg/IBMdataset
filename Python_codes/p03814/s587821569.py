s=input()
t,b=0,len(s)-1
while s[t]!='A':
	t+=1
while s[b]!='Z':
	b-=1
print(b-t+1)
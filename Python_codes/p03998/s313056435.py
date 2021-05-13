s=[list(input()) for i in range(3)]
k=0
while 1:
	if len(s[k])>0:
		t=s[k].pop(0)
		k=0 if t=='a' else 1 if t=='b' else 2
	else:
		break
print('ABC'[k])
s=list(input())
L=[]
for i in range((len(s)+1)//2):
	L.append(s[2*i])

print(''.join(L))
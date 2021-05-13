x=input()
k=[]
t=[]
for i in range(len(x)):
	k.append(x[i])
for i in range(len(x)):
	t.append(x[len(x)-i-1])

if k==t:
	print('Yes')
else:
	print('No')
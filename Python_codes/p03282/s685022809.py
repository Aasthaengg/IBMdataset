S=list(input())
K=int(input())
a=b=0

for s in S:
	if s=='1':
		a+=1
	else:
		b=s
		break
if a>=K:
	print(1)
else:
	print(b)
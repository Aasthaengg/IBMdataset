k=int(input())
if(k%2==0 or k%5==0):
	print(-1)
else:
	s=7
	count=1
	while(s%k!=0):
		s=(10*s+7)%k
		count+=1
	print(count)


K=int(input())
m=0
count=1
chk=0
for i in range(K):
	m=(m*10+7)%K
	if m==0:
		print(count)
		chk=1
		break
	count+=1

if chk==0:
	print(-1)
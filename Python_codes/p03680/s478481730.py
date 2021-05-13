N=int(input())
L=[]
count=0
t=0
for i in range(N):
	L.append(int(input()))
while(1):
	count+=1
	if count>N+10:
		print(-1)
		exit()
	if L[t]==2:
		print(count)
		exit()
	else:
		t=L[t]-1
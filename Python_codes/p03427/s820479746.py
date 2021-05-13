def digits_sum(N):
	sum=0
	while N/10!=0:
		sum+=N%10
		N//=10
	return sum
	
N=input()
N=list(N)
for k in range(len(N)):
	N[k]=int(N[k])
ans=0
pos=0
for i in range(1,len(N)):
	if N[i]!=9:
		N[i-1]=N[i-1]-1
		pos=i
		break
if pos==0:
	print(sum(N))
else:
	for j in range(pos):
		ans+=N[j]
	ans+=9*(len(N)-pos)
	print(ans)
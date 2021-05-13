n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
	# if(k%i==0):
	score=i
	tmp=0
	while(score<k):
		score=score*2
		tmp=tmp+1
	ans=ans+pow(0.5,tmp)
ans=ans/n
print(ans)

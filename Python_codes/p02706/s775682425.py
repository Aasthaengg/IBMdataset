n,m=list(map(int ,input().split()))
a=list(map(int ,input().split()))
s=0
for i in range(0,len(a)):
	s+=a[i]
if(s>n):
	print(-1)
	
elif(s<n):
	hangout=n-s
	print(hangout)
		
elif(s==n):
	print(0)

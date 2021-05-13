N=int(input())
ans=0

for i in range(1,N+1):
	cnt=0
	if i%2!=0:
		for h in range(1,i+1):
			if i%h==0:cnt+=1
		
	if cnt==8:ans+=1

print(ans)
n,m=map(int,input().split())
a=list(map(int,input().split()))
 
cnt=0
 
for i in a:
	if (sum(a)/(4*m))<=i:
		cnt+=1
		if cnt==m:
			print("Yes")
            
if cnt<m:
	print("No")
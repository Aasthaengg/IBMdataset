#dp[i]denotes who will win if i stones left
l=input().split()
n=int(l[0])
k=int(l[1])
l=input().split()
li=[int(i) for i in l]
hashi=dict()
for i in li:
	hashi[i]=1
m=min(li)
dp=[0 for i in range(k+1)]
dp[0]=2
for i in range(1,k+1):
	if(i<m):
		dp[i]=2
	done=0
	for j in hashi:
		if(i>=j and dp[i-j]==2):
			done=1
			break
	dp[i]=2-done
if(dp[k]==1):
	print("First")
else:
	print("Second")

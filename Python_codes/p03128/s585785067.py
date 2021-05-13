N,M=[int(x) for x in input().split()]
X=[0,2,5,5,4,5,6,3,7,6]
#    1,2,3,4,5,6,7,8,9

A=[int(x) for x in input().split()]



ANS=[0]
for i in range(1,N+1):
	ans=0
	for j in A:
		if i==X[j]:
			ans=max(j,ans)
		elif i>=X[j]:
			temp=ANS[i-X[j]]
			if temp!=0:

				ans=max(ans,10*temp+j)
		
		#print(ans)
	ANS.append(ans)
print(ANS[-1])
	

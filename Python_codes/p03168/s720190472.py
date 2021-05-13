n=int(input())
p=list(map(float,input().split(" ")))
mat=[]

for i in range(n):
	temp=[0]*(i+1+1)
	if(i==0):
		temp[0]=1-p[0]
		temp[1]=p[0]
	else:
		prev=mat[-1]

		for j in range(len(prev)):
			temp[j]+=prev[j]*(1-p[i])
			temp[j+1]+=prev[j]*p[i]


	mat.append(temp)
ans=0
temp=mat[-1]
for i in range((n//2)+1,len(temp)):
	ans+=temp[i]
# print(temp)
print(ans)
n= int(input())
L=list(map(int,input().split()))
ans=[]
p=0
for i in range(1,n-1,2):
	p+=L[i]

ans.append(sum(L)-2*p)

for i in range(1,n):
	ans.append(2*L[i-1]-ans[i-1])

print(*ans)
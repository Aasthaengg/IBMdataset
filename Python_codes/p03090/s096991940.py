n=int(input())
node=[[1]*n for _ in range(n)]
for i in range(n):
	node[i][i]=0
if n%2==0:
	for i in range(n//2):
		node[i][n-1-i]=0
		node[n-1-i][i]=0
else:
	for i in range(n//2):
		node[i][n-2-i]=0
		node[n-2-i][i]=0
ans=[]
for i in range(n):
	for j in range(i+1,n):
		if node[i][j]==1:
			ans.append((i,j))
print(len(ans))
for x,y in ans:
	print(x+1,y+1)
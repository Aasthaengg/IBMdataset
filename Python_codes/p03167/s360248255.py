mod=10**9+7
h,w=map(int,input().split())
grid=[]
for  i in range(h):
	a=input()
	grid.append(list(a))

grid[0][0]=1
for i in range(1,h):
	if(grid[i-1][0]==0):
		grid[i][0]=0
	elif(grid[i][0]=='#'):
		grid[i][0]=0
	else:
		grid[i][0]=grid[i-1][0]
for i in range(1,w):
	if(grid[0][i-1]==0):
		grid[0][i]=0
	elif(grid[0][i]=='#'):
		grid[0][i]=0
	else:
		grid[0][i]=grid[0][i-1]

for i in range(1,h):
	for j in range(1,w):
		if(grid[i][j]=='#'):
			grid[i][j]=0
		else:
			grid[i][j]=(grid[i][j-1]+grid[i-1][j])%mod
print(grid[h-1][w-1])
# import pprint
# grid.insert(0,grid)
# pprint.pprint(grid)

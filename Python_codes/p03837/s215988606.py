def main():
	n,m=map(int,input().split())
	inf=10**15
	dis=[[inf for _ in range(n)]for _ in range(n)]
	for i in range(n):
		dis[i][i]=0
	node=[]
	for i in range(m):
		a,b,c=map(int,input().split())
		dis[a-1][b-1]=c
		dis[b-1][a-1]=c
		node.append((a-1,b-1,c))
	for i in range(n):
		for j in range(n):
			for k in range(n):
				dis[j][k]=min(dis[j][k],dis[j][i]+dis[i][k])
	ans=0
	for x in node:
		f=0
		for i in range(n-1):
			if f:
				break
			for j in range(i+1,n):
				if dis[i][j]==dis[i][x[0]]+x[2]+dis[x[1]][j]:
					f=1
					break
				elif dis[i][j]==dis[i][x[1]]+x[2]+dis[x[0]][j]:
					f=1
					break
		if f==0:
			ans+=1
	print(ans)
if __name__ == '__main__':
	main()

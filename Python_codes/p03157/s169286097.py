h,w=map(int,input().split())
s=[]
for _ in range(h):
	s.append(input())
num=[[-1]*w for _ in range(h)]
stack=[]
def dfs():
	while stack:
		r=stack.pop()
		for x in ((1,0),(-1,0),(0,1),(0,-1)):
			a,b,c,d=r[0],r[1],x[0],x[1]
			if 0<=a+c<h and 0<=b+d<w:
				if s[a+c][b+d]!=s[a][b] and num[a+c][b+d]==-1:
					num[a+c][b+d]=num[a][b]
					stack.append((a+c,b+d))
color=0
for i in range(h):
	for j in range(w):
		if num[i][j]==-1:
			stack.append((i,j))
			num[i][j]=color
			dfs()
			color+=1
color_num=[[0,0]for _ in range(color)]
for i in range(h):
	for j in range(w):
		if s[i][j]==".":
			color_num[num[i][j]][0]+=1
		else:
			color_num[num[i][j]][1]+=1
ans=0
for x in color_num:
	ans+=x[0]*x[1]
print(ans)
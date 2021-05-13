N,M=map(int,input().split())
e=[int(x)-1 for x in input().split()]
p=[i for i in range(N)]
r=[0]*N

def find(x):
	if p[x]!=x:
		p[x]=find(p[x])
	return p[x]

def unite(x,y):
	x=find(x)
	y=find(y)
	if x==y:
		return

	if r[x]<r[y]:
		p[x]=y
	else:
		p[y]=x
		if r[x]==r[y]:
			r[x]+=1

def same(x,y):
	return find(x)==find(y)

for i in range(M):
	x,y=map(int,input().split())
	unite(x-1,y-1)

c=0
for i in range(N):
	if same(i,e[i]):
		c+=1

print(c)

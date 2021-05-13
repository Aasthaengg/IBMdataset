h , w = map(int, input().split())
c=[[] for i in range(10)]
for i in range(10):
	c[i] = list(map(int,input().split()))

mp=[[0]*10 for i in range(10)]

for i in range(10):
	for j in range(10):
		for k in range(10):
			c[j][k]=min(c[j][k],c[j][i]+c[i][k])

a=[[] for i in range(h)]

for i in range(h):
	a[i] = list(map(int,input().split()))
ans=0
for i in range(h):
	for j in range(w):
		if a[i][j]!=-1:
			ans+=c[a[i][j]][1]
print(ans)

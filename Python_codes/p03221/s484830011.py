n,m=map(int,input().split())
pys=[0]*m
for i in range(m):
	p,y=map(int,input().split())
	pys[i]=(p,y,i)
pys.sort(key=lambda x:x[1])

num=[0]*n
ans=[0]*m
for p,y,i in pys:
	num[p-1]+=1
	ans[i]=str(p).zfill(6)+str(num[p-1]).zfill(6)

for a in ans:
	print(a)
n,m=map(int,input().split())
xyz=[]
for _ in range(n):
	x,y,z=map(int,input().split())
	xyz.append([x,y,z])
def two(i):
	return "0"*(3-len(bin(i)[2:]))+bin(i)[2:]
ans=0
for i in range(8):
	p=two(i)
	for j in range(3):
		if p[j]=="1":
			for k in range(n):
				xyz[k][j]*=-1
	now=0
	xyz.sort(key=lambda x:-sum(x))
	for j in range(m):
		now+=sum(xyz[j])
	ans=max(ans,now)
	for j in range(3):
		if p[j]=="1":
			for k in range(n):
				xyz[k][j]*=-1
print(ans)
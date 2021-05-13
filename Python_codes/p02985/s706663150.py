#53 ABC133E
n,k=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n-1)]

mod=10**9+7

path=[[] for i in range(n)]
for a,b in ab:
	path[a-1].append(b-1)
	path[b-1].append(a-1)

abc=[False for _ in range(n)]

abc[0]=True
c=0
ans=k
t=[] 

for i in range(len(path[0])):
	child=path[0][i]
	if abc[child]:
		continue
	ans=ans*(k-1-c)%mod
	c+=1
	abc[child]=True
	t.append(child)
while len(t)>0:
	a=t.pop()
	c=0
	for i in range(len(path[a])):
		child=path[a][i]
		if abc[child]:
			continue
		ans=ans*(k-2-c)%mod
		c+=1
		abc[child]=True
		t.append(child)
print(ans%mod)
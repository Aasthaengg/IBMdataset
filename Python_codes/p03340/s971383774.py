n=int(input())
a=list(map(int,input().split()))
r=max(a)
e=len(bin(r))-2
p=[[]for _ in range(n)]
for i in range(e):
	for j in range(n):
		p[j].append(a[j]%2)
		a[j]//=2
ans=0
cnt=[0]*e
j=0
for i in range(n):
	while 2 not in cnt and j<n:
		for k in range(e):
			cnt[k]+=p[j][k]
		j+=1
	if 2 not in cnt:
		ans+=1
	ans+=j-i-1
	for k in range(e):
		cnt[k]-=p[i][k]
print(ans)
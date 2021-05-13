n,*L=map(int,open(0).read().split())
G=[[]for _ in range(n)]
db=[-1]*n;db[0]=0
dw=[-1]*n;dw[-1]=0
for a,b in zip(*[iter(L)]*2):
	G[a-1]+=[b-1]
	G[b-1]+=[a-1]
q=[0]
while q:
	cur=q.pop(0)
	for nxt in G[cur]:
		if db[nxt]<0:
			q.append(nxt)
			db[nxt]=db[cur]+1
q=[n-1]
while q:
	cur=q.pop(0)
	for nxt in G[cur]:
		if dw[nxt]<0:
			q.append(nxt)
			dw[nxt]=dw[cur]+1
b=w=0
for i,j in zip(db,dw):
	if i<=j:b+=1
	else:w+=1
if b<=w:print("Snuke")
else:print("Fennec")
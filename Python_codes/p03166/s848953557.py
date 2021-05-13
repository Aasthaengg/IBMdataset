import sys
sys.setrecursionlimit(10**6)
def f(x):
	global hashi
	if(x in hashi):
		return hashi[x]
	if(adj[x]==[]):
		return 0
	mino=0
	for i in adj[x]:
		mino=max(mino,f(i))
	hashi[x]=mino+1
	return mino+1
l=input().split()
n=int(l[0])
m=int(l[1])
adj=[[] for i in range(n+1)]
for i in range(m):
	l=input().split()
	u=int(l[0])
	v=int(l[1])
	adj[u].append(v)
maxa=0
hashi=dict()
for i in range(1,n+1):
	maxa=max(maxa,f(i))
print(maxa)

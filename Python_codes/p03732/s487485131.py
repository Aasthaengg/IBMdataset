N,W,*L=map(int,open(0).read().split())
w1=L[0]
l=[[] for _ in range(4)]
for w,v in zip(*[iter(L)]*2):
	l[w-w1].append(v)
l=[sorted(t)[::-1] for t in l]
a,b,c,d=map(len,l)
ans=0
for h in range(a+1):
	for i in range(b+1):
		for j in range(c+1):
			for k in range(d+1):
				if w1*h+(w1+1)*i+(w1+2)*j+(w1+3)*k<=W:
					ans=max(ans,sum(l[0][:h]+l[1][:i]+l[2][:j]+l[3][:k]))
print(ans)
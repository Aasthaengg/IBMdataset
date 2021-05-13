from itertools import*
n,c,*L=map(int,open(0).read().split())
a=[0]*(max(L[1::3])+1)
bef=(0,0)
for c,s,t in sorted((c,s,t) for s,t,c in zip(*[iter(L)]*3)):
	a[s-1+(bef==(c,s))]+=1
	a[t]-=1
	bef=(c,t)
print(max(accumulate(a)))
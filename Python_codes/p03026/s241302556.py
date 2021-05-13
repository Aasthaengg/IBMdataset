n,*t=map(int,open(0).read().split())
c=sorted(t[-n:])
q=[1]
f=q*-~n
e=[[]for _ in f]
for a,b in zip(t[:-n:2],t[1:-n:2]):e[a]+=b,;e[b]+=a,
while q:
 v=q.pop();n-=1;f[v]=c[n]
 for w in e[v]:q+=[w]*(f[w]<2)
print(sum(c[:-1]),*f[1:])
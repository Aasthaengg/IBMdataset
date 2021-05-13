n,*t=map(int,open(0).read().split())
c=sorted(t[-n:])
q=[1]
f=q*n
e=[[]for _ in f+q]
for a,b in zip(t[:-n:2],t[1:-n:2]):e[a]+=b,;e[b]+=a,
while q:v=q.pop();n-=1;f[v-1]=c[n];q+=[w for w in e[v]if f[w-1]<2]
print(sum(c[:-1]),*f)
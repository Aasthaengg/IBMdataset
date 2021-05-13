n,*t=map(int,open(0).read().split())
c=sorted(t[-n:])
print(sum(c[:-1]))
e={i:[]for i in range(n)}
for a,b in zip(t[:-n:2],t[1:-n:2]):e[a-1]+=b-1,;e[b-1]+=a-1,
f=[0]*n
q=[0]
while q:
 v=q.pop();f[v]=c.pop()
 for w in e[v]:q+=[w]*(f[w]<1)
print(*f)
(n,k),p,c=[[*map(int,t.split())]for t in open(0)]
a=-9e9
for i in range(n):
 s=f=0;x,j,*l=i,k
 while~f:x=p[x]-1;s+=c[x];l+=s,;f-=x==i
 for t in l[:k]:j-=1;a=max(a,t+j//len(l)*s*(s>0))
print(a)
n,*d=map(int,open(0).read().split());f=[d[i]-d[n+i]for i in range(n)];m=[v for v in f if v<0];p=sorted(v for v in f if v>0);c=len(m);s=sum(m)
while s<0and p:s+=p.pop();c+=1
print([c,-1][s<0])
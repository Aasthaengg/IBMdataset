from scipy.misc import comb
N,A,B,*V=map(int,open(0).read().split());d={}
for v in V:d[v]=d.get(v,0)+1
l=sorted(d.items(),key=lambda x:x[0])[::-1]
if l[0][1]>A:
 print(l[0][0])
 print(int(sum(comb(l[0][1],i,exact=1)for i in range(A,B+1))))
else:
 s=0;c=A
 for k,v in l:
  if v<c:s+=k*v;c-=v
  else:print((s+k*c)/A);print(int(comb(v,c,exact=1)));break
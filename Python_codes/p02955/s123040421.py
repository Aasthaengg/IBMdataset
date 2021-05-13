n,k,*l=map(int,open(0).read().split());s=sum(l);L=[]
for i in range(1,int(s**0.5)+1):
  if s%i==0:L+=[i,s//i]
for d in sorted(L)[::-1]:
  a=sorted([m%d for m in l])
  if sum(a[:n-sum(a)//d])<=k:print(d);exit()
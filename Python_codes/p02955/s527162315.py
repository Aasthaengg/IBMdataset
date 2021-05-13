n,k,*l=map(int,open(0).read().split())
s=sum(l)
L=[]
for i in range(1,30000):L+=[i,s//i]*(s%i<1)
L.sort()
for d in L[::-1]:
 a=sorted([m%d for m in l])
 if sum(a[:n-sum(a)//d])<=k:print(d);exit()
n,k,*l=map(int,open(0).read().split())
s=sum(l)
L=[]
for i in range(1,30000):L+=[i,s//i]*(s%i<1)
t=1
for d in L:a=sorted([m%d for m in l]);t=max(t,d*(sum(a[:-sum(a)//d])<=k))
print(t)
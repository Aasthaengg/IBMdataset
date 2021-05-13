n,k,*a=map(int,open(0).read().split())
s=sum(a)
b=[]
for i in range(1,30000):b+=[s//i,i]*(s%i<1)
m=1
for i in b:c=sorted(j%i for j in a);m=max(m,i*(sum(c[:-sum(c)//i])<=k))
print(m)
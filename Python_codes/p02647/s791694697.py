n,k,*a=map(int,open(0).read().split())
r=range(n)
for _ in a[:k][:41]:
 b=[0]*n*3
 for i in r:b[max(0,i-a[i])]+=1;b[i-~a[i]]-=1
 for i in r:b[i+1]+=b[i]
 a=b
print(*a[:n])
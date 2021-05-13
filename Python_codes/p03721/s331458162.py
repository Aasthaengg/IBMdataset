n,k=map(int,input().split())
ab=sorted([list(map(int,input().split()))for i in range(n)])
c=0
for i in ab:
 a,b=i[0],i[1];c+=b
 if c>=k:exit(print(a))
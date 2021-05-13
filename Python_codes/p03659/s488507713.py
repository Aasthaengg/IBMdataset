n,*a=map(int,open(0).read().split())
ans=10**100
b=sum(a)
c=0
for i in a[:-1]:
   c+=i
   b-=i
   ans=min(ans,abs(b-c))
print(ans)
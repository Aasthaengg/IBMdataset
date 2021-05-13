n,*a=map(int,open(0).read().split())
b=sum(a)
c=a[0]
ans=abs(2*c-b)
for i in a[1:-1]:
    c+=i
    ans=min(ans,abs(2*c-b))
print(ans)
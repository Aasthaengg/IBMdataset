n,a,b=map(int,input().split())
x=n//(a+b)
y=n-(a+b)*x
ans=a*x
if y>=a:
    ans+=a
else:
    ans+=y
print(ans)
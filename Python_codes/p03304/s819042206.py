n,m,d=map(int, input().split())
ans=0
if n-2*d>0:
    b=n-2*d
    a=2*d
else:
    a=(n-d)*2
    b=0
x1=(2*b+a)/(n**2)
if d!=0:
    ans=x1*(m-1)
else:
    ans=x1*(m-1)/2
print(ans)
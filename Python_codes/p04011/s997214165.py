n,k,x,y=(int(input()) for i in range(4))
if n<=k:
    ans=n*x
else:
    ans=k*x+(n-k)*y
print(ans)
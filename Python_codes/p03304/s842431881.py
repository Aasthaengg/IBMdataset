n,m,d=map(int,input().split())
ans=(n-d)*(m-1)/(n*n)
if d>0:
  ans*=2
print(ans)
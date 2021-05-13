n,m,k=map(int,input().split())
ans="No"
for i in range(n+1):
  if (2*i-n)==0:
    if k==m*n//2:
      ans="Yes"
  else:
    if (k-n*m+m*i)%(2*i-n)==0 and 0<=(k-n*m+m*i)//(2*i-n)<=m:
      ans="Yes"
print(ans)
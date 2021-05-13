n,a,b=map(int,input().split())
if a%2==b%2:
  print(abs((a+b)//2-a))
else:
  k=min(a-1,n-b)
  if a-1<n-b:
    flag=0
  else:
    flag=1
  if flag==0:
    if b-k-1>=0:
      print(k+1+abs(b-k-1-(1+b-k-1)//2))
    else:
      print(k+1)
  else:
    if a+k+1<=n:
      print(k+1+abs(a+k+1-(n+a+k+1)//2))
    else:
      pritn(k+1)
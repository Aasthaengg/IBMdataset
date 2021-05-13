n,k=map(int,input().split())
x=0
for b in range(k+1,n+1):
  r=n%b
  if r==0:
    x+=(n//b)*(b-k)
  else:  
    x+=(n//b+1)*max(0,(r-k+1))
    x+=(n//b)*max(0,(b-max(k,r+1)))
    if k==0:
      x-=1
print(x)
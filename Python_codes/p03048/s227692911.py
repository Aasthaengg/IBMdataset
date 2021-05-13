r,g,b,n=map(int,input().split())

rr=n//r+1
gg=n//g+1
bb=n//b+1
ans=0
for i in range(rr):
  for j in range(gg):
    x=i*r+j*g
    if (x>n):
      break
    if (n-x)%b==0:
      ans+=1
print(ans)
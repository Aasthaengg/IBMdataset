r,g,b,n=map(int,input().split())
c=0
for i in range(3001):
  for j in range(3001):
    if (n-i*r-j*g)%b==0 and 0<=n-i*r-j*g:
      c+=1
print(c)      
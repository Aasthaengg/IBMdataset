r,g,b,n=map(int,input().split())
X=0
for i in range(0,n+1,r):
  for j in range(0,n+1,g):
    k=n-i-j
    if k>=0 and k%b==0 and k<=n:
      X+=1
print(X)
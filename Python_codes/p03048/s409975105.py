R,G,B,n=map(int,input().split())
r=n//R
g=n//G
b=n//B
ans=0
for i in range(r+1):
  for j in range((n-R*i)//G+1):
    if (n-i*R-j*G)%B==0:
      ans+=1
print(ans)
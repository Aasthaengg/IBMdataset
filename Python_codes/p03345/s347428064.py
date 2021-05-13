a,b,c,k=map(int,input().split())
abc=a+b+c
k2=k%2
if k2==0:
  ans=a-b
else:
  ans=b-a
print(ans)
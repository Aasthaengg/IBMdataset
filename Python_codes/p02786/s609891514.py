n=int(input())
ans=0
while n>1:
  n=n//2
  ans+=1
  
ans1=2**(ans+1)-1
print(ans1)
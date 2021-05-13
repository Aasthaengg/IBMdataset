n=int(input())
a=list(map(int,input().split()))

mod=10**9+7
a.sort()

if n%2==0:
  b=[]
  for i in range(n//2):
    b.append((i*2+1))
    b.append((i*2+1))
  if a==b:
    ans=1
    for _ in range(n//2):
      ans=ans*2
      ans=ans%mod
      
    print(ans)
    
  else:
    print(0)
    
else:
  b=[0]
  for i in range((n-1)//2):
    b.append(((i+1)*2))
    b.append(((i+1)*2))
    
  if a==b:
    ans=1
    for i in range((n-1)//2):
      ans=ans*2
      ans=ans%mod
      
    print(ans)
      
  else:
    print(0)
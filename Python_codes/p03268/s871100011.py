N,M=list(map(int,input().split()))
ans=0
half=0
for i in range(1,N+1):
   if i%M==0:
      ans+=1
if M%2==0:
   for i in range(1,N+1):
      if i%M==M//2:
         half+=1
   print(ans**3+half**3)
else:
   print(ans**3)
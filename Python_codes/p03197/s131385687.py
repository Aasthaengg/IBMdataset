N=int(input())
a=[0]*N

ans=True
for i in range(N):
    a[i]=int(input())
    if a[i]%2==1:
      ans = False
      
if ans:
   print("second")
else:
  print("first")
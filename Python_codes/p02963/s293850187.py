s=int(input())
ans1=s//10**9+1
ans2=10**9-s%10**9
if s==10**18:
  print(0,0,10**9,0,0,10**9)
else:
  print(0,0,10**9,1,ans2,ans1)

s=int(input())
t=10**9
if s%t==0:
  print(0,0,1,t,s//t,0)
else:
  print(0,0,1,t,s//t+1,t-(s%t))
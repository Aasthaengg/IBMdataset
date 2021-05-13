k,t=map(int,input().split())
a=list(map(int,input().split()))
ma=max(a)
if ma >= sum(a)-ma+1:
  print(ma-(sum(a)-ma)-1)
else:
  print(0)
  
  

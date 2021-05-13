n=3
a=[0]*n
a[:]=map(int,input().split())
if sum(a)>=22:
  print("bust")
else:
  print("win")
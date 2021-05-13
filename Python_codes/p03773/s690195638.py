a=list(map(int,input().split()))
if sum(a)>=24:
  print(sum(a)%24)
else:
  print(sum(a))
a=input()
b=list(map(int,input().split()))
b.sort()
if sum(b)-max(b)-max(b)>0:
  print("Yes")
else:
  print("No")
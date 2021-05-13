input()
A=map(str,input().split())
if len(set(A))==4:
  print("Four")
else:
  print("Three")
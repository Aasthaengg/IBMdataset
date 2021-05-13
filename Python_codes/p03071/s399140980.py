A,B = map(int,input().split())
if(A == B):
  print(str(A * 2))
else:
  print(str(max(A,B) * 2 - 1))
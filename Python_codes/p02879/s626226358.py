A,B = input().split()
A = int(A)
B = int(B)
if(A < 10):
  if(B < 10):
    print(A*B)
  else:
    print(-1)
else:
  print(-1)
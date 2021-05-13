N,A,B=map(int,input().split())
 
if N==1:
  if A==B:
    print(1)
  else:
    print(0)
elif A==B:
  print(1)
elif A>B:
  print(0)
else:
  print(B*(N-2)-A*(N-2)+1)
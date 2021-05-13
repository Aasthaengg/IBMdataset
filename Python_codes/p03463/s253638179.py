N,A,B=map(int,input().split())
while True:
  if B!=A+1:
    A+=1
  else:
    if A==1:
      print("Borys")
      exit()
    else:
      A-=1
 
  if A!=B-1:
    B-=1
  else:
    if B==N:
      print("Alice")
      exit()
    else:
      B+=1
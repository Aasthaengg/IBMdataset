A,B=map(int,input().split())
if A==B:
  print("Draw")
elif (A==1) & (B!=1):
  print("Alice")
elif (B==1) & (A!=1):
  print("Bob")
elif (A>B):
  print("Alice")
elif (A<B):
  print("Bob")
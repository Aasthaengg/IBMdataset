a,b,c=map(int,input().split())
disA = abs(a-b)
disB = abs(a-c)
if disA < disB:
  print("A")
else:
  print("B")
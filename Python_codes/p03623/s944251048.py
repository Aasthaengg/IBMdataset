n=input().rstrip().split()
n=[int(x) for x in n]

if abs(n[1]-n[0])<abs(n[2]-n[0]):
  print("A")
else:
  print("B")
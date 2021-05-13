N=int(input())
for c in range(100//4+1):
  for d in range(100//7+1):
    if c*4+d*7==N:
      print("Yes")
      exit()
print("No")

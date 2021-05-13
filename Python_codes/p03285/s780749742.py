N = int(input())

for n in range(25):
  for m in range(25):
    if n*4+m*7==N:
      print("Yes")
      exit()
      
print("No")
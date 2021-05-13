n=int(input())
for i in range(9):
  if n<=i*111:
    print((i)*111)
    break
else:
  print(999)
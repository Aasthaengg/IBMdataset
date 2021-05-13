n=int(input())
for i in range(int((2*n)**0.5-3),n+2):
  if i*(i+1)//2==n:
    for j in range(1,i+1):
      print(j)
    break
  elif i*(i+1)//2>n:
    k=i*(i+1)//2-n
    for j in range(1,i+1):
      if j!=k:
        print(j)
    break

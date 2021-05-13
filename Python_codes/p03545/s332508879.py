A=list(input())
b=[]
for i in range(2**3):
  b.clear()
  for j in range(3):
    if (i>>j)&1:
      b.append("+")
    else:
      b.append("-")
  c=eval(A[0]+b[0]+A[1]+b[1]+A[2]+b[2]+A[3])
  if c==7:
    print(A[0]+b[0]+A[1]+b[1]+A[2]+b[2]+A[3]+"=7")
    exit()
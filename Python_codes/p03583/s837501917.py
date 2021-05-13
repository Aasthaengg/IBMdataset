n=int(input())
for i in range(1,3501):
  for j in range(1,3501):
    if 4*i*j-i*n-j*n!=0:
      k=(i*j*n)/(4*i*j-i*n-j*n)
      if k>0 and k.is_integer():
        print(i,j,int(k))
        exit(0)
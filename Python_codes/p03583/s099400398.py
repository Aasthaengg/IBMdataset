N=int(input())
if N%2==0:
  print(N//2,N,N)
else:
  for i in range(1,3501):
    for j in range(1,3501):
      if 4*i*j-N*i-N*j>0:
        if (N*i*j/(4*i*j-N*i-N*j)).is_integer():
          print(i,j,int((N*i*j/(4*i*j-N*i-N*j))))
          exit()
N=int(input())
for h in range(1,3501):
  for n in range(1,3501):
    if 4*h*n-N*n-N*h!=0:
      w=(N*n*h)/(4*h*n-N*n-N*h)
      if int(w)==w and w>0:
        print(h,n,int(w))
        exit()
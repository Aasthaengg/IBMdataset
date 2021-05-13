N=int(input())

for h in range(1,3501):
  for n in range(1,3501):
    tmp=4*h*n-N*n-N*h
    if tmp==0:
      continue
    else:
      w=N*h*n/tmp
      
    if w>0 and w.is_integer():
      print(h,n,int(w))
      exit()
N=int(input())
for h in range(1,3501):
  for n in range(1,3500):
    u=N*h*n
    s=4*h*n-N*n-N*h
    if s==0:continue
    if u%s==0:
      if u//s>0:
        print(h,n,u//s)
        exit()
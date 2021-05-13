import sys
N=int(input())
for h in range(1,3501):
  for n in range(h,3501):
    if 4*h*n-N*n-h*N>0 and (N*h*n)%(4*h*n-N*n-h*N)==0:
      ans=[]
      ans.append(str(h))
      ans.append(str(n))
      ans.append(str((N*h*n)//(4*h*n-N*n-h*N)))
      print(' '.join(ans))
      sys.exit()
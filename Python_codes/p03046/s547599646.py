m,k=map(int,input().split())
if k>=2**m:
  print(-1)
elif m==0:
  print(0,0)
elif m==1:
  if k==0:
    print(0,0,1,1)
  elif k==1:
    print(-1)
else:
  ris=[str(i) for i in range(2**m)]
  ris.remove(str(k))
  l=" ".join(ris)
  r=" ".join(ris[::-1])
  print(l,str(k),r,str(k))
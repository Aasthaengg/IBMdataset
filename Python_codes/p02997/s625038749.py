N,K=map(int,input().split())
if int((N-1)*(N-2)/2)<K:
 print(-1)
else:
 if N==2:
  print(1)
  print(*[1,2])
 else:
  S=int((N-1)*(N-2)/2)-K
  print(N-1+S)
  for i in range(N-1):
   print(*[1,2+i])
  t=0
  l=2
  r=3
  while t<S:
   print(*[l,r])
   t+=1
   if r==N:
    l+=1
    r=l+1
   else:
    r+=1

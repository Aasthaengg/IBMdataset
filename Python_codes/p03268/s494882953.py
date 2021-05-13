N,K=map(int,input().split())

if K%2:
  tmp0=0
  for i in range(1,N+1):
    if i%K==0:
      tmp0+=1
  print(tmp0**3)
else:
  tmp0=0
  tmp1=0
  for i in range(1,N+1):
    if i%K==0:
      tmp0+=1
    if i%K==K//2:
      tmp1+=1
  print(tmp0**3+tmp1**3)
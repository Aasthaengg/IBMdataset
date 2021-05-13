N=int(input())
H=list(map(int,input().split()))

if N==1:print('Yes')
else:
  MAX=H[0]
  ok=1
  for i in range(1,N):
    if H[i]>MAX:MAX=H[i]
    if H[i]<=MAX-2:
      ok=0
      break
  if ok==1:print('Yes')
  else:print('No')
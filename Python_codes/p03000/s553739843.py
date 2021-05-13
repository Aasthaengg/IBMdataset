N,X=map(int,input().split())
if N!=1:
  L=list(map(int,input().split()))
  tot=0
  count=1
  for i in range(N):
    tot+=L[i]
    if X>=tot:
      count+=1
  print(count)
else:
  L=int(input())
  if X>=L:
    print(2)
  else:
    print(1)
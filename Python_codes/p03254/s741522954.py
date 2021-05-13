a,b=map(int,input().split())
L=list(map(int,input().split()))
L=sorted(L)
ans=0
if sum(L)<b:
  print(a-1)
elif sum(L)==b:
  print(a)
else:
  for i in range(a):
    ans+=L[i]
    if ans>b:
      print(i)
      exit()
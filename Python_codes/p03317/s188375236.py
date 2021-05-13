n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=len(a)
ans-=k
if ans%(k-1)==0:
  print(ans//(k-1)+1)
else:
  print(ans//(k-1)+2)
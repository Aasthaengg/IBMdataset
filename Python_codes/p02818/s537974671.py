a,b,k=list(map(int, input().split()))
if a<k:
  k-=a
  a=0
  if b<k:
    b=0
  else:
    b-=k-a
else:
  a-=k
print(a,b)
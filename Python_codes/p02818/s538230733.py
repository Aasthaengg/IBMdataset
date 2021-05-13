a,b,k=[int(x) for x in input().split()]
if a>=k:
  a-=k
  print(str(a)+' '+str(b))
else:
  k-=a
  a=0
  if b>=k:
    b-=k
    print(str(a)+' '+str(b))
  else:
    b=0
    print("0 0")
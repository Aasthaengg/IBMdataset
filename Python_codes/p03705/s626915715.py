n,a,b=[int(_) for _ in input().split()]
if n==1:
  if a==b:
    print(1)
  else:
    print(0)
  exit()
print(max(0,(n-2)*(b-a)+1))

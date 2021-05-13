n,p = map(int,input().split())
a = [int(i) for i in input().split()]
if all([i%2 == 0 for i in a]):
  if p == 1:
    print(0)
  else:
    print(pow(2,n))
else:
  print(pow(2,n-1))
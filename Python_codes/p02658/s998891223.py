a=int(input())
b=list(map(int,input().split()))
c=1
b.sort()
if b[0]==0:
  print(0)
else:
  for i in range(a):
    c=c*b[-i]
    if c>1000000000000000000:
      break
  if c>1000000000000000000:
    print(-1)
  else:
    print(c)
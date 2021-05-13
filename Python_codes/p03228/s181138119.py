a,b,k = map(int,input().split())
while True:
  if k == 0:
    print(a,b)
    break
  else:
    a,b = a//2,b+a//2
    k -= 1
  if k == 0:
    print(a,b)
    break
  else:
    a,b = a+b//2,b//2
    k -= 1
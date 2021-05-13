n = int(input())
if n&1:
  print(0)
else:
  i = 1
  c = 0
  n=n//2
  while True:
    t = n//(5**i)
    if t==0:
      break
    c+=t
    i+=1
  print(c)
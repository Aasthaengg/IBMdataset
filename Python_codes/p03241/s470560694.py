n,m = map(int,input().split())
if m%n==0:
    print(int(m//n))
    exit()
else:
  a = m/n
  l = []
  for i in range(int(m**0.5),0,-1):
    if m%i==0:
      l.append(i)
      l.append(m//i)
  l = sorted(l)[::-1]
  for j  in l:
    if j<=a:
      print(j)
      exit()
  else:
    print(1)
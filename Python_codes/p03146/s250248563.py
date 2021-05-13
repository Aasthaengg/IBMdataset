s = int(input())
a = [s]

for n in range(1000000):
  if a[n]%2==0:
    if int(a[n]/2) not in a:
      a.append(int(a[n]/2))
    else:
      print(n+2)
      exit()
  else:
    if int(3*a[n]+1) not in a:
      a.append(int(3*a[n]+1))
    else:
      print(n+2)
      exit()
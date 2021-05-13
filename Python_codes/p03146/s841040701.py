n=int(input())

l=[n]
while True:
  if n%2==0:
    n=n/2
    if n in l:
      print(len(l)+1)
      break
    l.append(n)
  else:
    n=3*n+1
    if n in l:
      print(len(l)+1)
      break
    l.append(n)
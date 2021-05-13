input()
A=list(map(int,input().split()))
r=1
if 0 not in A:
  for a in A:
    r*=a
    if r>10e17:
      print(-1)
      break
  else:
    print(r)
else:
  print(0)
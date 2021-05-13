h=list(map(int,input().split()))
w=sorted(h)
if (w[1]-w[0])==(w[2]-w[1]):
  print('YES')
else:
  print('NO')
NAB=list(map(int,input().split()))
m=NAB[0]*NAB[1]

if m>NAB[2]:
  print(NAB[2])
else:
  print(m)
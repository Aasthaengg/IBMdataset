N,R = (int(i) for i in input().split())

tmp = 100*(10-N)

if tmp >= 0:
  print(100*(10-N) + R)
else:
  print(R)

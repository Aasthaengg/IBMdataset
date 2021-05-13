r,d,x = map(int, raw_input().split(' '))
q = 10
while(q):
  x = r*x - d
  print x
  q-=1



while 1:
  x, y = map(int, raw_input().split())
  if x == y == 0:
     break


  if x < y:
     print '%d %d' %(x, y)
  elif x > y :
     print '%d %d' %(y, x)
  elif x == y:
     print '%d %d' %(x, y)

 
a,b,c = (int(x) for x in input().split())
if a == b:
  if a == c:
    print (1)
  else:
    print (2)
else:
  if a == c:
    print (2)
  else:
    if b == c:
      print (2)
    else:
      print (3)
l = [int(x) for x in input().split()]
if l[2]==l[0]+l[1] or l[0]==l[1]+l[2] or l[1]==l[0]+l[2]:
  print ('Yes')
else:
  print ('No')

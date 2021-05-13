l = [int(x) for x in input().split(' ')]
if l[0]%3 == 0 or l[1]%3==0 or (l[0]+l[1])%3==0:
  print("Possible")
else:
  print("Impossible")

l = list(map(int, input().split()))
l.sort()
if l[2]%2 == 0:
  print(0)
else:
  print(l[0]*l[1])
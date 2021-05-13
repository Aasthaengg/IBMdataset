X,Y = map (int, input ().split ())
p = 0
if X == 1:
  p += 300000
elif X == 2:
  p += 200000
elif X == 3:
  p += 100000
if Y == 1:
  p += 300000
elif Y == 2:
  p += 200000
elif Y == 3:
  p += 100000
if X == Y == 1:
  p += 400000
print (p)
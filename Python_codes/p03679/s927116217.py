X, A, B = map(int, input().split())

if (A-B) >= 0:
  print("delicious")
elif (A-B) >= (-1)*X:
  print("safe")
else:
  print("dangerous")
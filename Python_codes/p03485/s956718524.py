a, b = map(int, input().split())

mean = (a+b)/2
if mean > int(mean):
  print(int(mean)+1)
else:
  print(int(mean))
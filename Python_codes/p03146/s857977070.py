s = int(input())
i = 1
if s == 1 or s == 2:
  print(4)
  exit()
while True:
  if s == 4:
    print(i+3)
    exit()
  if s%2 == 0:
    s=s//2
  else:
    s=3*s+1
  i += 1
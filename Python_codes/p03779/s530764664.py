x = int(input())

i = 0

while True:
  tmp = int((i*(i+1))/2)
  if tmp >= x:
    print(i)
    exit()
  else:
    i += 1
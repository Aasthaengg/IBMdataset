n = int(input())

while True:
  tmp = str(n)
  if(tmp[0] == tmp[1] == tmp[2]):
    print(n)
    break
  else:
    n += 1
n = int(input())
for i in range(1000):
  if i < 100:
    continue
  else:
    tmp = i
    if (tmp%10 == (tmp//10)%10 == (tmp//100)%10) and i >= n:
      print(i)
      break
    else:
      continue
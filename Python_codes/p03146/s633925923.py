s = int(input())
cnt = 0
if s!=1 and s!=2:
  cnt = 0
  while s != 4:
    if s % 2 == 0:
      s = s / 2
    else:
      s = 3 * s + 1
    cnt += 1
print(cnt+4)
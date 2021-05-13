s = int(input())
n = 1
while 1:
  if s == 1 or s == 2 or s == 4:
    print(n+3)
    break
  if s % 2 == 1:
    s = 3 * s + 1
  else:
    s //= 2
  n += 1
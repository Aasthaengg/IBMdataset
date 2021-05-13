N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
n = 0
for gift in a:
  n += 1
  x -= gift
  if n < len(a):
    if x < 0:
      break
    else:
      i += 1
  elif n == len(a):
    if x == 0:
      i += 1
    else:
      break


print(i)
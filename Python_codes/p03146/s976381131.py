s = int(input())
A = []
i = 2
while True:
  A.append(s)
  if s%2 == 0:
    s = s // 2
  else:
    s = 3*s + 1

  if s in A:
    print(i)
    exit()

  i += 1
n = int(input())
cnt = 0
def sympy(num):
  l = []
  for i in range(1, num+1):
    for j in range(1, num+1):
      if (i % 2 != 0) and (i*j == num):
        l.append(i)
  return l
for i in range(1, n+1):
  l = sympy(i)
  if (i % 2 != 0) and (len(l) == 8):
    cnt += 1
print(cnt)
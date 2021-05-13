a = int(input())
l = []
i = 0
while a not in l:
  l.append(a)
  if a%2 == 0:
    a //= 2
  else:
    a = 3*a + 1
  i += 1
print(i+1)
n = int(input())
l_10 = []
l_else = []
for i in range(n):
  s = int(input())
  if s % 10 == 0:
    l_10.append(s)
  else:
    l_else.append(s)

if len(l_else) > 0:
  if sum(l_else) % 10 == 0:
    print(sum(l_else)-min(l_else)+sum(l_10))
  else:
    print(sum(l_else)+sum(l_10))
else:
  print(0)
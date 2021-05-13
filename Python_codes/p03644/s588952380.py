N = int(input())
pi = 0
for n in range(1, N+1):
  i = 0
  dn = n
  while dn % 2 == 0:
    i += 1
    dn = dn / 2
    if dn % 2 == 1:
      break
  
  if i >= pi:
    result = n
    pi = i
  else:
    pass
  

print(result)
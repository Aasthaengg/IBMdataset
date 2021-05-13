N = int(input())
p = [int(i) for i in input().split()]

cnt = 0
for i in range(N):
  for j in range(i+1,N):
    temp = 0
    good = True
    for k in range(N):
      if k == i:
        if temp > p[j]:
          good = False
          break
        else:
          temp = p[j]
      elif k == j:
        if temp > p[i]:
          good = False
          break
        else:
          temp = p[i]
      else:
        if temp > p[k]:
          good = False
          break
        else:
          temp = p[k]
    if good:
      break
  if good:
    break

temp = 0
good2 = True
for k in range(N):
    if temp > p[k]:
      good2 = False
      break
    else:
      temp = p[k]
    
if good or good2:
  print('YES')
else:
  print('NO')
N = int(input())
L = [[] for _ in range(1000)]
l = 0
r = 1
for i in range(1, N+1):
  L[l].append(i)
  L[r].append(i)
  if(r-l == 1):
    r += 1
    l = 0
  else:
    l += 1
if(l != 0):
  print('No')
else:
  print('Yes')
  print(r)
  for i in range(r):
    print(len(L[i]), *L[i])
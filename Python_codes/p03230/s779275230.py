N = int(input())

x = (1+(1+8*N)**0.5)/2
if x.is_integer():
  print('Yes')
  x = int(x)
  print(x)
  S = [[] for _ in range(x)]
  e = 1
  for i in range(x):
    for j in range(i+1,x):
      S[i].append(e)
      S[j].append(e)
      e += 1
  for s in S:
    print(len(s),*s)
else:
  print('No')
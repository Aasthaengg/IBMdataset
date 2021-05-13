N, x = map(int, input().split())
L = list(map(int, input().split()))
l = sorted(L)
c = 0
if sum(L) < x:
  print(len(l)-1)
else:
  for i in range(N):
    if x < l[i]:
      break
    x = x - l[i]
    c += 1
    
  print(c)
N = int(input())
L =[]
l2 = []
for _ in range(N):
   L.append(int(input()))
ma = max(L)

if L.count(ma) > 1:
  [print(ma) for _ in range(N)]
else:  
  for i in L:
    if i == ma:
      print(sorted(L)[-2])
    else:
      print(ma)
n = int(input())
B = [int(i) for i in input().split()]
ans = []

while B:
  L = []
  for i in range(len(B)):
    if B[i] == i+1:
      L.append(B[i])
      
  if L:
    ans.append(L[-1])
    B.pop(L[-1]-1)
  else:
    print(-1)
    exit()
  
for i in ans[::-1]:
  print(i)
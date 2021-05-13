r,d,x = map(int, input().split())

L = [x]
for i in range(1,11):
  L.append(L[i-1]*r - d)
  
L.pop(0)
for i in range(len(L)):
  print(L[i])

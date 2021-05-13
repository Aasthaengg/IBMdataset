w = str(input())
L = []
for i in w:
  L.append(i)
if len(L) % 2 == 1:
  print('No')
  exit()
L.sort()
for j in range(0,len(L),2):
  if L[j] != L[j + 1]:
    print('No')
    exit()
print('Yes')
  

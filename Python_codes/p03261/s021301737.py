n = int(input())
ar = []

for i in range(n):
  ar.append(input())


for i in range(n-1):
  
 
  if ar[i][-1] != ar[i+1][0]:
    print('No')
    exit()
  if ar.count(ar[i])>1:
    print('No')
    exit()
print('Yes')
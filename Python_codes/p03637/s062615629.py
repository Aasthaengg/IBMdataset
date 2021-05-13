N = int(input())
A = list(map(int, input().split()))
l1 = 0
l2 = 0
l4 = 0
for i in range(len(A)):
  if(A[i] % 4 == 0):
    l4 += 1
  elif(A[i] % 2 == 0):
    l2 += 1
  else:
    l1 += 1
if(l2 == 0 and l4 + 1 == l1):
  print('Yes')
elif(l4 < l1):
  print('No')
else:
  print('Yes')


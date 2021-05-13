import numpy as np

N = int(input().rstrip())
L = [int(i) for i in input().rstrip().split()]
L.sort(reverse = True)

L = np.array(L)
x = L[0]
y = np.sum(L)-L[0]

if x<y:
  print('Yes')
else:
  print('No')
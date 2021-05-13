N = list(input())
n = len(N)
X = 0
k = 0
for i in range(0, n):
  X += int(N[i])

if X % 9 == 0:
  print('Yes')
else:
  print('No')


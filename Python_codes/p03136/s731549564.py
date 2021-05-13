N = int(input())
L = list(map(int,input().split()))

L.sort(reverse = True)
sum = 0

for i in range(N-1):
  sum += L[i+1]
  
if L[0] < sum:
  print('Yes')
else:
  print('No')
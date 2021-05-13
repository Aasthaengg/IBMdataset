import math

N = int(input())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

if sum(As) > sum(Bs):
  print('No')
  exit()
  
dif = sum(Bs) - sum(As)
A = 0
for i in range(N):
  if Bs[i] > As[i]:
    A += math.ceil((Bs[i]-As[i])/2)
    
if A > dif:
  print('No')
else:
  print('Yes')
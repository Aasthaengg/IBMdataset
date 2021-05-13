import math
N = int(input())
A = list(map(int,input().split()))
A.reverse()
l = 2
r = 2
for i in range(N):
  l = math.ceil(l/A[i])*A[i]
  r = math.floor(r/A[i])*A[i]+A[i]-1
if r >= l:
  print(l,r)
else:
  print(-1)
H, N = map(int,input().split())
A = list(map(int,input().split()))
T = 0
for i in range(N):
  T += A[i]
if H-T <=0:
  print('Yes')
else:
  print('No')
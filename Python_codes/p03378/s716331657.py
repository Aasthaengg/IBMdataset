N,M,X = map(int,input().split())
A = list(map(int,input().split()))
min = 0
max = 0
for i in range(M):
  if A[i] < X:
    min += 1
  else:
    max += 1
if min < max:
  print(min)
else:
  print(max)
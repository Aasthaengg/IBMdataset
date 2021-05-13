N , X = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
a = 0
for i in range(N):
  a += A[i]
  if a > X:
    break
if i == N - 1:
  if a == X:
    print(i + 1)
  else:
    print(i)
if i < N - 1:
  print(i)

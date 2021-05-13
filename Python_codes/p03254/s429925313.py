N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
SUM = 0
f = 0
for i in range(N):
  SUM += A[i]
  if SUM > x:
    print(i)
    f = 1
    break
if f == 0:
  if SUM == x:
    print(N)
  else:
    print(N-1)
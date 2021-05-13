N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = 0
for n in range(N):
  if n == 0:
    c += min(A[0], B[0])
    temp = c
  else:
    c += min(A[n] - temp, B[n])
    temp = min(A[n] - temp, B[n])
  c += min(A[n+1], B[n] - temp)
  temp = min(A[n+1], B[n] - temp)
print(c)
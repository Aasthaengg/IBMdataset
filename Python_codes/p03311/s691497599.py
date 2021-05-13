def mm(N, A, x):
  S = 0
  for i in range(N):
    S += abs(A[i] - x)
  return S

N = int(input())
A = []
j = 0
for i in input().split():
  j += 1
  A.append(int(i)-j)
A.sort()
if N % 2 == 0:
  print(mm(N, A, A[N//2]))
elif N == 1:
  print(0)
else:
  print(min(mm(N, A, A[N//2]), mm(N, A, A[N//2 + 1])))
MOD = 10**9+7
n = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
C = [0]*n
if T[0] > A[0] or T[-1] < A[-1]:
  print(0)
  exit()
C[0], C[-1] = 1, 1
for i in range(1, n-1):
  if T[i-1] == T[i]:
    t = -T[i]
  else:
    t = T[i]
  if A[i] == A[i+1]:
    a = -A[i]
  else:
    a = A[i]
  if t > 0 and a > 0:
    if t != a:
      print(0)
      exit()
    C[i] = 1
  else:
    if t > 0:
      if t > abs(a):
        print(0)
        exit()
      C[i] = 1
    elif a > 0:
      if a > abs(t):
        print(0)
        exit()
      C[i] = 1
    else:
      C[i] = min(-t, -a)
ans = 1
for i in C:
  ans *= i
  ans %= MOD
print(ans)
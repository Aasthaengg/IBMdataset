N = int(input())
A = list(map(int, input().split()))
A.sort()
M = A[0]
X = [A[0]]
pos = N
for i in range(N):
  if A[i] >= 0:
    pos = i
    break
if pos == 0:
  for i in range(1, N - 1):
    M -= A[i]
    X.append(M)
  S = M
  M = A[N-1] - M
  print(M)
  for i in range(N - 2):
    print(X[i], A[i+1])
  print(A[N - 1], S)
elif 1 <= pos <= N - 1:
  M = sum(abs(_) for _ in A)
  print(M)
  L = A[0]
  for j in range(pos, N - 1):
    print(L, A[j])
    L -= A[j]
  R = A[N - 1]
  print(R, L)
  R -= L
  for j in range(1, pos):
    print(R, A[j])
    R -= A[j]
elif pos == N:
  print(A[N-1] - sum(A[i] for i in range(N-1)))
  R = A[N - 1]
  for i in range(N-1):
    print(R, A[i])
    R -= A[i]
N, M = map(int, input().split())
X, Y, Z = [0]*N, [0]*N, [0]*N
for i in range(N):
  X[i], Y[i], Z[i] = map(int, input().split())

U = [0] * N
answer = []
for i in range(2):
  for j in range(2):
    for k in range(2):
      for n in range(N):
        U[n] = X[n]*(-1)**i + Y[n]*(-1)**j + Z[n]*(-1)**k
      U.sort()
      U = U[::-1]
      answer.append(sum(U[:M]))
print(max(answer))
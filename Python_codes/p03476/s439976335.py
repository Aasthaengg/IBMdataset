N = 10 ** 5
D = [0] * (N + 1)
for i in range(2, N + 1):
  if(D[i] == 0):
    for j in range(i, N + 1, i):
      if(D[j] == 0):
        D[j] = i

T = [0] * (N + 1)
for i in range(3, N, 2):
  if(D[i] == i and D[i + 1] == 2 and D[(i + 1) // 2] == (i + 1) // 2):
    T[i] = 1
S = [0] * (N + 1)

for i in range(N):
  S[i + 1] = S[i] + T[i + 1]

Q = int(input())
for i in range(Q):
  l, r = list(map(int, input().split()))
  print(S[r] - S[l - 1])
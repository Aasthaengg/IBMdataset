N, A, B = map(int, input().split())
L = list(map(int, input().split()))
D = [A * (L[i+1] - L[i]) for i in range(N - 1)]
S = 0
for i in range(N - 1):
  if D[i] > B:
    S += B
  else:
    S += D[i]
print(S)
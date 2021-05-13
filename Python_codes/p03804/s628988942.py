N, M = map(int, input().split())
A = list(input() for _ in range(N))
B = list(input() for _ in range(M))
b = len(B[0])

ans = "No"
for i in range(N-(M-1)):
  n = -1
  c = 0
  for j in range(M):
    if B[j] in A[i+j]:
      if n < 0:
        n = A[i + j].index(B[j])
        c += 1
      else:
        if B[j] in A[i + j][n: n + b + 1]:
          c += 1
  if c == M:
    ans = "Yes"
print(ans)
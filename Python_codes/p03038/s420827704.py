N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = []
for i in range(M):
  b, c = map(int, input().split())
  B.append([c, b])
B.sort(reverse=True)
i = 0
f = 0
for j in range(M):
  while B[j][1]:
    if A[i] < B[j][0]:
      A[i] = B[j][0]
      B[j][1] -= 1
      i += 1
      if i >= N:
        f = 1
        break
    else:
      f = 1
      break
  if f == 1:
    break
print(sum(A))
N = int(input())
A = list(map(int, input().split()))

L = [A[0]]
for i in range(1, N):
  if A[i] != A[i - 1]:
    L.append(A[i])

N = len(L)

if N == 1:
  print(1)
  exit()

f = L[1] > L[0]
ans = 1

i = 2
while i < N:
  if (L[i] > L[i - 1]) != f:
    ans += 1
    if i == N - 1:
      break
    i += 1
    f = L[i] > L[i - 1]

  i += 1
 
print(ans)
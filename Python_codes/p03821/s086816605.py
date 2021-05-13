N = int(input())
A, B = [0]*N, [0]*N
for i in range(N):
  A[i], B[i] = map(int, input().split())

button = 0
for i in range(N)[::-1]:
  q, mod = divmod(A[i], B[i])
  if mod != 0:
    button += (q + 1) * B[i] - A[i]
  if i - 1 >= 0:
    A[i - 1] += button

print(button)
N = int(input())
A = list(map(int, input().split()))
for i in range(1 , 10 ** 20):
  for j in range(N):
    a = A[j] % (2 ** i)
    if a != 0:
      break
  if a != 0:
    break
print(i - 1)
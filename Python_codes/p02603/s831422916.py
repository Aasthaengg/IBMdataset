N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0
for i in range(N-1):
  for j in range(i+1, N):
    if A[i] > A[j]:
      money += stock * A[i]
      stock = 0
      break

    if A[i] < A[j]:
      stock += money // A[i]
      money -= A[i] * (money // A[i])
      break

money += stock * A[-1]
print(money)

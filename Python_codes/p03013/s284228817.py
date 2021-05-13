N, M = list(map(lambda n: int(n), input().split(" ")))

fibonacci = [1, 1, 2]
for i in range(1, N + 1):
  fibonacci.append((fibonacci[i] + fibonacci[i + 1]) % 1000000007)

fibonacci.append(1)
fibonacci.append(0)

A = [-1]
for i in range(M):
  A.append(int(input()))
A.append(N + 1)

ans = 1
# 1 23 45 67 89 (101)
# 0 -> 0
# 2 -> 22
# 24 -> 44
# 46 -> 66
# fibonacci(A[i + 1] - 2 - A[i])

for i in range(len(A) - 1):
  ans *= fibonacci[A[i+1]-A[i]-2] % 1000000007
  ans = ans % 1000000007
print(ans)
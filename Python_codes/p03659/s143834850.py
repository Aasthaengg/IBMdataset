N = int(input())
A = list(map(int, input().split()))
m = sum(A)

ans = 10 ** 15
now = 0
for i in range(N):
  now += A[i]
  if (i != N - 1):
    ans = min(ans, abs(m - 2 * now))

print(ans)

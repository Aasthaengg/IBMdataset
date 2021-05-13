N = int(input())
A = list(map(int, input().split()))
x = sum(A) * 1.0 / N
ans = 0
m = 10000
for i in range(N):
  n = abs(x - A[i])
  if m > n:
    m = n
    ans = i
print(ans)
N = int(input())
A = list(map(int, input().split()))

tmp = [0 for i in range(N+1)]
length = 0
for i in range(N):
  tmp[i+1] = tmp[i] + A[i]
  length += A[i]
  
ans = 10 ** 10
for i in range(1, N+1):
 ans = min(ans, abs((length - tmp[i]) - tmp[i]))

print(ans)

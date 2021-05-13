K, N = map(int, input().split())
A = list(map(int, input().split()))

diff = [0]*N
diff[N-1] = A[0] + K - A[N-1]
for i in range(N-1):
  diff[i] = A[i+1] - A[i]

ans = sum(diff) - max(diff)
print(ans)
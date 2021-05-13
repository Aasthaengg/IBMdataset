N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * 200001
for i in range(N):
  L[A[i]] += 1
L.sort(reverse = True)
ans = 0
for i in range(K):
  ans += L[i]
print(N-ans)
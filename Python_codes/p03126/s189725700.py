N, M = map(int, input().split())
ans = set(range(1, M+1))
for i in range(N):
  K, *A = map(int, input().split())
  ans = ans & set(A)
print(len(ans))
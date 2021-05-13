N = int(input())
def f(i):
  return sum([int(j) for j in str(i)])
ans = float('inf')
for A in range(1, N):
  B = N - A
  ans = min(ans, f(A) + f(B))
print(ans)
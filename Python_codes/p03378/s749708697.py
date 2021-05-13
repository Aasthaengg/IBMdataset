N, M, X = map(int, input().split())
A = list(map(int, input().split()))
c = [0 for i in range(N+1)]
for a in A:
  c[a] = 1
ans = sum(c[:X+1])
print(min(ans, M-ans))
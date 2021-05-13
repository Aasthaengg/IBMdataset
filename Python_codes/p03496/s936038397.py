N = int(input())
A = list(map(int, input().split()))
min_a, max_a = min(A), max(A)
min_idx, max_idx = A.index(min_a)+1, A.index(max_a)+1

ans = []
if abs(min_a) <= abs(max_a):
  for i in range(1, N+1):
    ans.append([max_idx, i])
  for i in range(1, N):
    ans.append([i, i+1])
else:
  for i in range(1, N+1):
    ans.append([min_idx, i])
  for i in range(N, 1, -1):
    ans.append([i, i-1])

print(len(ans))
for a in ans:
  print(*a)
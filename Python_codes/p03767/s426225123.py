N = int(input())
A = sorted(list(map(int, input().split())))[::-1]

ans = 0
for i, a in enumerate(A[: - N]):
  if i % 2 == 1:
    ans += a
    
print(ans)

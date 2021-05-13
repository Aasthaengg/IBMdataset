N = int(input())
A = list(map(int, input().split()))
m = A[0]
ans = 0
for a in A:
  m = min(m, a)
  if m == a:
    ans += 1
print(ans)
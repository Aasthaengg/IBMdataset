n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for e in arr:
  if e >= k:
    ans += 1
print(ans)
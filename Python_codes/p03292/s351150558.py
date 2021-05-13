a = sorted(map(int, input().split()))
ans = 0
for i, j in zip(a, a[1:]):
  ans += abs(j - i)
print(ans)

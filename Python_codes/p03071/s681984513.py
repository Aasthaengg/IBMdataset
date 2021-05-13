data = list(map(int, input().split()))

ans = 0
for _ in range(2):
  p = data.index( max(data) )
  ans += data[p]
  data[p] -= 1

print(ans)

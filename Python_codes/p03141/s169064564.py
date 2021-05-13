n = int(input())
AB = [tuple(map(int, input().split())) for _ in range(n)]
AB.sort(key = lambda x : x[0] + x[1], reverse = 1)
ans = 0
for i in range(n):
  a, b = AB[i]
  if i & 1:
    ans -= b
  else:
    ans += a
print(ans)
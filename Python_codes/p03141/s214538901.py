n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
C = sorted([(i+j, i, j) for i,j in AB], reverse=True)
ans = 0
for i in range(n):
  s, t, a = C[i]
  if i%2 == 0:
    ans += t
  else:
    ans -= a
print(ans)
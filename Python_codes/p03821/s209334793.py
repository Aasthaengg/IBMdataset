N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(-1, -N - 1, -1):
  a, b = AB[i]
  m = (a + ans) % b
  if m != 0:
    ans += b - m

print(ans)
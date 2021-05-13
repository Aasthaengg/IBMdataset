N = int(input())
AB = [list(map(int, input().split())) for i in range(N)][::-1]

ans = 0
for a, b in AB:
  d = (a + ans) % b
  if d: ans += b - d

print(ans)
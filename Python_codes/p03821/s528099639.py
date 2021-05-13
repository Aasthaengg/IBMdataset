N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
AB.reverse()
ans = 0
for a, b in AB:
  ans += (- a - ans) % b
print(ans)

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1, -1, -1):
  a = ab[i][0]
  b = ab[i][1]
  if (a+ans) % b != 0:
    ans += b-(a+ans)%b
print(ans)
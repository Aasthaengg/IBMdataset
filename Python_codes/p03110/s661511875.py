
n = int(input())
xu = [list(input().split()) for i in range(n)]
ans = 0
for i in range(n):
  if xu[i][1] == "BTC":
    ans += float(xu[i][0]) * 380000
  else:
    ans += int(xu[i][0])

print(ans)
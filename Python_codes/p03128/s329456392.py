N, M = map(int, input().split())
a = list(map(int, input().split()))
mn = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

msort = lambda s: -s[0]

b = list(map(lambda i: [i, mn[i]], a))
b.sort(key = msort)
dp = [-100] * (N + 1)
dp[0] = 0
for i in range(2, N + 1):
  for n in b:
    if i >= n[1] and dp[i - n[1]] >= 0:
      dp[i] = max([dp[i], dp[i - n[1]] + 1])

match = N
ans = ''
while match > 0:
  for n in b:
    if match >= n[1] and dp[match] == dp[match - n[1]] + 1:
      ans += str(n[0])
      match -= n[1]
      break
    
print(ans)
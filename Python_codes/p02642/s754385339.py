from collections import Counter
n = int(input())
a= list(map(int,input().split()))
if n == 1:
  print(1)
  exit()

a.sort()

c = Counter(a)
a = list(set(a))
dp = [0] * (10**6 +1)

for x in a:
  t = x * 2
  while t <= 10**6:
    dp[t] = 1
    t += x

ans = 0
for x in a:
  if (c[x] == 1) & (dp[x] == 0):
    ans += 1

print(ans)

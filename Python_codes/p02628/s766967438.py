n, k = map(int, input().split())
money = [int(x) for x in input().split()]
ans = 0

money.sort()

for i in range(k):
  ans += money[i]
print(ans)
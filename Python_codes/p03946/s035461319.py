N, T = map(int, input().split())
A = list(map(int, input().split()))

# i番目の町以降の取引金額の最大値
# 末尾はダミー
righter_max = [0] * (N+1)
for i, a in enumerate(A[::-1], 2):
  righter_max[-i] = righter_max[-i+1]
  if righter_max[-i] < a:
    righter_max[-i] = a

ans = 0
max_profit = 0
for i, a in enumerate(A, 1):
  profit = righter_max[i] - a
  if profit == max_profit:
    ans += 1
  elif profit > max_profit:
    max_profit = profit
    ans = 1

print(ans)
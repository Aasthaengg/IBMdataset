# D - Road to Millionaire
def sell(asset, price):
  return price * asset[1] + asset[0]


def buy(money, price):
  stock = money // price
  remainder = money % price
  
  return (remainder, stock)


from collections import deque
import copy

N = int(input())
A = list(map(int, input().split()))

# タプルのキュー
assets = deque()
assets.append((1000, 0))

for i in range(N - 1):
  new_assets = deque()
  max_money = 0
  
  for a in assets:
    max_money = max(max_money, sell(a, A[i]))  
  
  assets.append((max_money, 0))
  assets.append(buy(max_money, A[i]))

ans = 0

for a in assets:
  ans = max(ans, sell(a, A[N - 1]))

print(ans)
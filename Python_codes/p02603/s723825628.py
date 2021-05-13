# D - Road to Millionaire
def sell(price):
  global money
  global stock
  
  money += price * stock
  stock = 0


def buy(price):
  global money
  global stock

  stock += money // price
  money %= price


N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0

for i in range(N - 1):
  if A[i] < A[i + 1]:
    sell(A[i])
    buy(A[i])
  elif A[i + 1] < A[i]:
    sell(A[i])

sell(A[N - 1])

print(money)
N = int(input())
A = list(map(int, input().split()))

def sell(money,stock,price):
  money += price*stock
  stock = 0
  return money, stock

def buy(money,price):
  stock,money = divmod(money,price)
  return money,stock

money = 1000
stock = 0
for i in range(N):
  money, stock = sell(money,stock,A[i])
  if i<N-1 and A[i]<A[i+1]:
    money, stock = buy(money,A[i])
print(money)
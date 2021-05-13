n = int(input())
a = list(map(int, input().split()))
money = 1000
for i in range(n-1):
  stocks = 0
  if a[i] < a[i+1]:
    stocks = money // a[i]
    money += (a[i+1] - a[i]) * stocks
print(money)
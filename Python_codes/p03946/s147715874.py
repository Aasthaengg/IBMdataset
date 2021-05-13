n, t = map(int, input().split(" "))
list_a = list(map(int, input().split(" ")))
list_profit = []
min_price = list_a[0]
for a in list_a:
  if min_price < a:
    list_profit.append(a - min_price)
  else:
    list_profit.append(0)
    min_price = a
max_profit = max(list_profit)
print(list_profit.count(max_profit))
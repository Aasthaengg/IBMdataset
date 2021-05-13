stock = {}
for _ in range(int(input())):
  s = input()
  try:
    stock[s] += 1
  except KeyError:
    stock[s] = 1
print(len(stock))
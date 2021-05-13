n = int(input())

c = list(input())

red = c.count('R')
white = n - red
redinred = 0
whiteinred = 0

for i in range(red):
  if c[i] == 'W':
    whiteinred += 1
  else:
    redinred += 1

redinwhite = red - redinred

trade = min(whiteinred, redinwhite)
change = abs(whiteinred - redinwhite)

print(trade + change)
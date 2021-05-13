cards_mirror = []
cards_shaffled = []
k = 0
try:
  while True:
    k += 1
    cards = list(input())
    n_irritation = int(input())
    if cards[0] == '-':
      break
    for i in range(n_irritation):
      n_shaffled = int(input())
      cards_mirror = cards.copy()
      for j in range(len(cards)):
        cards[j] = cards_mirror[(j+n_shaffled)%len(cards)]
    cards_shaffled.append(cards)
except EOFError:
  pass
for i in range(len(cards_shaffled)):
  for j in range(len(cards_shaffled[i])):
    print(cards_shaffled[i][j],end='')
  print('')

def game(card) : 
  player = 'a'
  while True :
    if len(card[player]) == 0 : 
      break
    player = card[player].pop(0)
  return player.upper()


card = dict()

card['a'] = list(input())
card['b'] = list(input())
card['c'] = list(input())

print(game(card))
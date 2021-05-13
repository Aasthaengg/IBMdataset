from collections import Counter

blue_cards = [input() for _ in range(int(input()))]
red_cards = Counter([input() for _ in range(int(input()))])

sources = set(blue_cards)
blue_cards = Counter(blue_cards)

result = 0
for x in sources:
  tmp = blue_cards[x]
  
  if x in red_cards:
    tmp -= red_cards[x]
  
  result = max(result, tmp)
  
print(result)
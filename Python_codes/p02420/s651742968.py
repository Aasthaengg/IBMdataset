while True:
  card=input()
  if card =="-":
    break
  
  k=input()
  kai=int(k)
  
  for i in range(kai):
    s=int(input())
    card=card[s:]+card[:s]
  print(card)

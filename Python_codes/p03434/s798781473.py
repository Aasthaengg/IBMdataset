n = input()
cards = list(map(int,input().split(" ")))
cards = sorted(cards,reverse=True)
a ,b = 0,0
for i in range(len(cards)):
  if i % 2 == 0:
    a += cards[i]
  else:
    b += cards[i]
print(a-b)
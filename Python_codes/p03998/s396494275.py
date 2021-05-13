A, B, C =[input() for _ in range(3)]
T = {"a":A, "b":B, "c":C}
player = "a"
card = "a"
while len(T[player])>0:
  card = T[player][0]
  T[player] = T[player][1:]
  player = card
else:
  print(player.upper())
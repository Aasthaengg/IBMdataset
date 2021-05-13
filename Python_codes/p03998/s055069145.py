A = list(input())
B = list(input())
C = list(input())

A.append("#")
B.append("#")
C.append("#")
game = {
  "A" : A,
  "B" : B,
  "C" : C
}
turn = "A"
finished = False

while not finished:
  next_turn = game[turn].pop(0)
  if next_turn == "#":
    print(turn)
    finished = True
  else:
    turn = next_turn.upper()

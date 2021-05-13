from collections import deque

A = list(input())
B = list(input())
C = list(input())

CARDS = [deque(A),deque(B),deque(C)]
s_to_i = {"a":0,"b":1,"c":2}
turn = 0

while CARDS[turn]:
  nxt = CARDS[turn].popleft()
  turn = s_to_i[nxt]
  
if turn == 0:
  print("A")
elif turn == 1:
  print("B")
elif turn == 2:
  print("C")


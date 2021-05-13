cards = {}
for _ in range(int(input())):
  s = input()
  cards[s] = cards.get(s,0)+1
for _ in range(int(input())):
  t = input()
  cards[t] = cards.get(t,0)-1
print(max(max(cards.values()),0))
# -*- coding: utf-8 -*-
# 整数の入力
N = int(input())
cards = [int(s) for s in input().split()]

alice_total = 0
bob_total = 0

cards.sort(reverse=True)

for i in range(len(cards)):
  if i % 2 == 0:
    alice_total += cards[i]
  else:
    bob_total += cards[i]

diff = alice_total - bob_total
print(diff)

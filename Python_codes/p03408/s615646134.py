cards = {}

n = int(input())
for _ in range(n):
    s = input()
    cards[s] = cards.get(s,0)+1

m = int(input())
for _ in range(m):
    t = input()
    cards[t] = cards.get(t,0)-1

print(max(max(cards.values()),0))


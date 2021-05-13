from __future__ import division, print_function
from sys import stdin
while True:
    cards = stdin.readline().rstrip()
    if cards.startswith('-'):
        break
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        cards = cards[n:] + cards[:n]
    print(cards)
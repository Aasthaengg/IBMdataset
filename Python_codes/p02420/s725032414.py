#!/usr/bin/env python

contents = []

while True:
    text = input()
    if text == '-':
        break
    m = int(input())
    hArray = []
    for i in range(m):
        h = int(input())
        hArray.append(h)
    contents.append([text, hArray])

for x in contents:
    deck = x[0]
    for i in x[1]:
        deck = deck[i:] + deck[:i]
    print(deck)
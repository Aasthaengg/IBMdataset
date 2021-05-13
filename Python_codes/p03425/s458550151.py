#! env/bin/local python3
# -*- coding: utf-8 -*-

import itertools

n = int(input())
names = []
march = {
    'M': 0,
    'R': 0,
    'A': 0,
    'C': 0,
    'H': 0
}

while True:
    try:
        names.append(input())
    except EOFError:
        break


for name in names:
    try:
        march[name[0]] += 1
    except KeyError:
        continue

patterns = list(itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3))

total = 0
for pattern in patterns:
    total += march[pattern[0]] * march[pattern[1]] * march[pattern[2]]

print(total)
# author:  Taichicchi
# created: 25.09.2020 21:12:29

import sys

X = int(input())

for a in range(300):
    for b in range(-300, 300):
        if (a ** 5 - b ** 5) == X:
            print(a, b)
            exit()

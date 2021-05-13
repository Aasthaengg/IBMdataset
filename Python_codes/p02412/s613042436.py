import sys
from itertools import combinations

while True:
    c, n = map(int, raw_input().split())
    if c == n == 0:
        break

    # sum(cC3) == 9
    count = 0
    for i in combinations(range(1, c + 1),3):
        if sum(i) == n:
            count += 1
    print count
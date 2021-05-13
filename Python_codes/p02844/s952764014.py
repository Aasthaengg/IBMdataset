#create date: 2020-08-11 09:28

import sys
stdin = sys.stdin
from itertools import product

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    s = ns()
    ans = 0

    for a in product(range(10), repeat=3):
        i = 0
        for si in s:
            if int(si) == a[i]:
                i += 1
            if i == 3:
                ans += 1
                break
    print(ans)

if __name__ == "__main__":
    main()
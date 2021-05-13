#create date: 2020-06-29 13:18

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    v = na()
    c = na()
    ans = 0
    for vi, ci in zip(v, c):
        ans += max(0, vi-ci)
    print(ans)

if __name__ == "__main__":
    main()
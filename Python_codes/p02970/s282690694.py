#create date: 2020-07-07 11:00

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, d = na()
    m = 2 * d + 1
    print((n-1)//m + 1)

if __name__ == "__main__":
    main()
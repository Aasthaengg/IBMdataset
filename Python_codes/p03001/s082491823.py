#create date: 2020-06-29 13:35

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    w, h, x, y = na()
    print("{:.10f} {}".format(w*h/2, 1 if w/2==x and h/2==y else 0))

if __name__ == "__main__":
    main()
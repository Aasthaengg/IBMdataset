#create date: 2020-06-29 13:18

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b, t = na()
    print(b  * (t // a))

if __name__ == "__main__":
    main()
#create date: 2020-06-29 13:35

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    x, a = na()
    print(0 if x<a else 10)

if __name__ == "__main__":
    main()
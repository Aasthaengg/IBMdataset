#create date: 2020-06-30 09:30

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b = na()
    print(a*b)

if __name__ == "__main__":
    main()
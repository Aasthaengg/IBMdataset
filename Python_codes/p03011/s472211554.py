#create date: 2020-07-25 09:12

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a = na()
    print(sum(a) - max(a))

if __name__ == "__main__":
    main()
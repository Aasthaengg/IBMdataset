#create date: 2020-08-11 09:28

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, _ = na()
    b, _ = na()
    print(b-a)

if __name__ == "__main__":
    main()